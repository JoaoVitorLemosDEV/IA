import unittest
from robo import *

class TesteClimaBot(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.robo = configurar_robo()
        return super().setUpClass()

    def testar_01_previsao_chuva_amanha(self):
        self.assertIsNotNone(self.robo)

        perguntas = [
            "vai chover amanhã?",
            "tem previsão de chuva para amanhã?",
            "amanhã vai ter chuva?",
            "o tempo indica chuva amanhã?"
        ]

        for pergunta in perguntas:
            resposta = self.robo.get_response(pergunta)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "possibilidade de chuva",
                resposta.text.lower()
            )

    def testar_02_temperatura_atual(self):
        self.assertIsNotNone(self.robo)

        perguntas = [
            "qual a temperatura atual?",
            "quanto está a temperatura agora?",
            "qual é a temperatura no momento?",
            "está fazendo quantos graus agora?"
        ]

        for pergunta in perguntas:
            resposta = self.robo.get_response(pergunta)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "temperatura atual",
                resposta.text.lower()
            )

    def testar_03_previsao_de_hoje(self):
        self.assertIsNotNone(self.robo)

        perguntas = [
            "mostrar previsão de hoje",
            "qual é a previsão do tempo para hoje?",
            "como está o clima hoje?",
            "me diga a previsão de hoje"
        ]

        for pergunta in perguntas:
            resposta = self.robo.get_response(pergunta)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "previsão para hoje",
                resposta.text.lower()
            )

    def testar_04_atualizar_dados_meteorologicos(self):
        self.assertIsNotNone(self.robo)

        perguntas = [
            "atualizar dados meteorológicos",
            "atualizar informações do clima",
            "puxar os dados meteorológicos mais recentes",
            "fazer a atualização das informações do tempo"
        ]

        for pergunta in perguntas:
            resposta = self.robo.get_response(pergunta)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "dados meteorológicos foram atualizados",
                resposta.text.lower()
            )

unittest.main()
