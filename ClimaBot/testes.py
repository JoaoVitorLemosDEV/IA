import unittest
from robo import *

class TesteClimaBot(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.robo = configurar_robo()
        return super().setUpClass()

    def testar_01_saudacoes_genericas(self):
        self.assertIsNotNone(self.robo)

        entradas = ["oi", "olá", "tudo bem?", "como vai?", "oi, tudo bem?", "olá, como vai?"]

        for entrada in entradas:
            resposta = self.robo.get_response(entrada)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "sou o climabot",
                resposta.text.lower()
            )

    def testar_02_bom_dia(self):
        entradas = ["bom dia", "olá, bom dia", "oi, bom dia"]

        for entrada in entradas:
            resposta = self.robo.get_response(entrada)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn("bom dia, sou o climabot", resposta.text.lower())

    def testar_03_boa_tarde(self):
        entradas = ["boa tarde", "olá, boa tarde", "oi, boa tarde"]

        for entrada in entradas:
            resposta = self.robo.get_response(entrada)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn("boa tarde, sou o climabot", resposta.text.lower())

    def testar_04_boa_noite(self):
        entradas = ["boa noite", "olá, boa noite", "oi, boa noite"]

        for entrada in entradas:
            resposta = self.robo.get_response(entrada)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn("boa noite, sou o climabot", resposta.text.lower())

    def testar_05_previsao_chuva_amanha(self):
        entradas = [
            "vai chover amanhã?",
            "tem previsão de chuva para amanhã?",
            "amanhã vai ter chuva?",
            "o tempo indica chuva amanhã?"
        ]

        for entrada in entradas:
            resposta = self.robo.get_response(entrada)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn("chuva", resposta.text.lower())

    def testar_06_temperatura_atual(self):
        entradas = [
            "qual a temperatura atual?",
            "quanto está a temperatura agora?",
            "qual é a temperatura no momento?",
            "está fazendo quantos graus agora?"
        ]

        for entrada in entradas:
            resposta = self.robo.get_response(entrada)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn("temperatura", resposta.text.lower())

    def testar_07_previsao_hoje(self):
        entradas = [
            "mostrar previsão de hoje",
            "qual é a previsão do tempo para hoje?",
            "como está o clima hoje?",
            "me diga a previsão de hoje"
        ]

        for entrada in entradas:
            resposta = self.robo.get_response(entrada)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn("previsão", resposta.text.lower())

    def testar_08_atualizar_dados_meteorologicos(self):
        entradas = [
            "atualizar dados meteorológicos",
            "atualizar informações do clima",
            "puxar os dados meteorológicos mais recentes",
            "fazer a atualização das informações do tempo"
        ]

        for entrada in entradas:
            resposta = self.robo.get_response(entrada)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn("atualiz", resposta.text.lower())

unittest.main()
