from nltk import word_tokenize, corpus
from inicializador_modelo import *
from threading import Thread
from transcritor import *
import secrets
import pyaudio
import wave
import json
import os
import torch
from time import sleep

from atuadores_meteorologicos import *

LINGUAGEM = "portuguese"
FORMATO = pyaudio.paInt16
CANAIS = 1
AMOSTRAS = 1024
TEMPO_GRAVACAO = 5
CAMINHO_AUDIO_FALAS = "temp"
CONFIGURACOES = "config.json"

if not os.path.exists(CAMINHO_AUDIO_FALAS):
    os.makedirs(CAMINHO_AUDIO_FALAS)

def iniciar(dispositivo):
    processador, modelo = iniciar_modelo(MODELOS[0], dispositivo)
    modelo_iniciado = processador is not None and modelo is not None
    gravador = pyaudio.PyAudio()
    palavras_de_parada = set(corpus.stopwords.words(LINGUAGEM))
    with open(CONFIGURACOES, "r", encoding="utf-8") as arquivo_configuracoes:
        configuracoes = json.load(arquivo_configuracoes)
        acoes = configuracoes["acoes"]
    return modelo_iniciado, processador, modelo, gravador, palavras_de_parada, acoes

def iniciar_atuadores():
    atuadores = []
    if iniciar_meteorologia():
        atuadores.append({
            "nome": "clima",
            "atuacao": atuar_sobre_clima
        })
    return atuadores

def capturar_fala(gravador):
    gravacao = gravador.open(format=FORMATO, channels=CANAIS, rate=TAXA_AMOSTRAGEM, input=True, frames_per_buffer=AMOSTRAS)
    fala = []
    for _ in range(0, int(TAXA_AMOSTRAGEM / AMOSTRAS * TEMPO_GRAVACAO)):
        fala.append(gravacao.read(AMOSTRAS))
    gravacao.stop_stream()
    gravacao.close()
    return fala

def gravar_fala(gravador, fala):
    gravado, arquivo = False, f"{CAMINHO_AUDIO_FALAS}/{secrets.token_hex(32).lower()}.wav"
    try:
        wav = wave.open(arquivo, "wb")
        wav.setnchannels(CANAIS)
        wav.setsampwidth(gravador.get_sample_size(FORMATO))
        wav.setframerate(TAXA_AMOSTRAGEM)
        wav.writeframes(b"".join(fala))
        wav.close()
        gravado = True
    except Exception as e:
        print(f"Erro gravando arquivo de fala: {str(e)}")
    return gravado, arquivo

def processar_transcricao(transcricao, palavras_de_parada):
    comando = []
    tokens = word_tokenize(transcricao)
    for token in tokens:
        if token not in palavras_de_parada:
            comando.append(token)
    return comando

def validar_comando(comando, acoes):
    for acao_prevista in acoes:
        acao = acao_prevista["nome"]
        dispositivo = acao_prevista["dispositivos"][0]
        if any(token.lower() in acao_prevista["palavras_chave"] for token in comando):
            return True, acao, dispositivo
    return False, None, None

def atuar(acao, dispositivo, atuadores):
    for atuador in atuadores:
        if atuador["nome"] == dispositivo:
            print(f"Enviando comando para {atuador['nome']}")
            Thread(target=atuador["atuacao"], args=[acao, dispositivo]).start()

def ativar_linha_de_comando():
    while True:
        print("\nFale alguma coisa...")
        fala = capturar_fala(gravador)
        gravado, arquivo = gravar_fala(gravador, fala)
        if gravado:
            fala_tensor = carregar_fala(arquivo)
            transcricao = transcrever_fala(dispositivo, fala_tensor, modelo, processador)
            if os.path.exists(arquivo):
                os.remove(arquivo)
            comando = processar_transcricao(transcricao, palavras_de_parada)
            print(f"Comando reconhecido: {comando}")
            valido, acao, dispositivo_alvo = validar_comando(comando, acoes)
            if valido:
                print(f"Executando {acao} sobre {dispositivo_alvo}")
                atuar(acao, dispositivo_alvo, atuadores)
            else:
                print("Comando inválido")
            sleep(1)
        else:
            print("Ocorreu um erro gravando a fala")

if __name__ == "__main__":
    dispositivo = "cuda:0" if torch.cuda.is_available() else "cpu"
    iniciado, processador, modelo, gravador, palavras_de_parada, acoes = iniciar(dispositivo)

    if iniciado:
        atuadores = iniciar_atuadores()
        ativar_linha_de_comando()
    else:
        print("Ocorreu um erro de inicialização")
