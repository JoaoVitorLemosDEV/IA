from assistente import *
import unittest
import torch

PREVISAO_HOJE = "audios/mostrar_previsao.wav"
VAI_CHOVER = "audios/vai_chover.wav"
TEMPERATURA_ATUAL = "audios/qual_a_temperatura.wav"
ATUALIZAR_DADOS = "audios/atualizar_dados.wav"

class Testes(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.dispositivo = "cuda:0" if torch.cuda.is_available() else "cpu"
        cls.iniciado, cls.processador, cls.modelo, _, cls.palavras_de_parada, cls.acoes = iniciar(cls.dispositivo)
        cls.atuadores = iniciar_atuadores()

    def testar_modelo_iniciado(self):
        self.assertTrue(self.iniciado)

    def _testar_comando(self, caminho_audio, acao_esperada):
        fala = carregar_fala(caminho_audio)
        self.assertIsNotNone(fala)

        transcricao = transcrever_fala(self.dispositivo, fala, self.modelo, self.processador)
        self.assertIsNotNone(transcricao)

        comando = processar_transcricao(transcricao, self.palavras_de_parada)
        self.assertIsNotNone(comando)

        valido, acao, dispositivo_alvo = validar_comando(comando, self.acoes)
        self.assertTrue(valido)
        self.assertEqual(acao, acao_esperada)
        self.assertEqual(dispositivo_alvo, "clima")

    def testar_mostrar_previsao(self):
        self._testar_comando(PREVISAO_HOJE, "mostrar_previsao")

    def testar_vai_chover(self):
        self._testar_comando(VAI_CHOVER, "vai_chover")

    def testar_temperatura_atual(self):
        self._testar_comando(TEMPERATURA_ATUAL, "temperatura_atual")

    def testar_atualizar_dados(self):
        self._testar_comando(ATUALIZAR_DADOS, "atualizar_dados")


if __name__ == "__main__":
    unittest.main()
