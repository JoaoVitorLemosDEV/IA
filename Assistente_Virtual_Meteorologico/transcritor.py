from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC
import torchaudio
import torch

MODELO = "lgris/wav2vec2-large-xlsr-open-brazilian-portuguese-v2"
TAXA_AMOSTRAGEM = 16_000

def iniciar_modelo(nome_modelo=MODELO, dispositivo="cpu"):
    try:
        processador = Wav2Vec2Processor.from_pretrained(nome_modelo)
        modelo = Wav2Vec2ForCTC.from_pretrained(nome_modelo).to(dispositivo)
        return processador, modelo
    except Exception as e:
        print(f"Erro ao iniciar o modelo: {str(e)}")
        return None, None

def carregar_fala(caminho_audio):
    audio, amostragem = torchaudio.load(caminho_audio)

    if audio.shape[0] > 1:
        audio = torch.mean(audio, dim=0, keepdim=True)

    if amostragem != TAXA_AMOSTRAGEM:
        resample = torchaudio.transforms.Resample(amostragem, TAXA_AMOSTRAGEM)
        audio = resample(audio)

    return audio.squeeze()

def transcrever_fala(dispositivo, fala, modelo, processador):
    with torch.no_grad():
        entrada = processador(fala, return_tensors="pt", sampling_rate=TAXA_AMOSTRAGEM).input_values.to(dispositivo)
        logits = modelo(entrada).logits
        predicao = torch.argmax(logits, dim=-1)
        transcricao = processador.batch_decode(predicao)[0]
    return transcricao.lower().strip()
