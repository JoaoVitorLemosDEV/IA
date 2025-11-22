import unittest
from robo import *

class TesteSaudacoes(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.robo = configurar_robo()
        return super().setUpClass()

    def testar_01_oi_ola(self):
        self.assertIsNotNone(self.robo)

        saudacoes = ["oi", "olá", "tudo bem?", "como vai?"]
        for saudacao in saudacoes:
            resposta = self.robo.get_response(saudacao)

            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn("Olá, sou o IFBA-Bot, um robô de atendimento do IFBA, o que você gostaria de saber sobre o IFBA?".lower(), resposta.text.lower())

    def testar_02_bom_dia_tarde_noite(self):
        self.assertIsNotNone(self.robo)

        saudacoes = ["bom dia", "boa tarde", "boa noite"]
        for saudacao in saudacoes:
            resposta = self.robo.get_response(saudacao)

            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(f"{saudacao}! Sou o IFBA-Bot, um robô de atendimento do IFBA, o que você gostaria de saber sobre o IFBA?".lower(), resposta.text.lower())

    def testar_03_variabilidades(self):
        self.assertIsNotNone(self.robo)

        variabiliades = ["oi, tudo bem?", "olá, como vai?","ola, tudo bem?", "oi. como vai?"]
        for variabilidade in variabiliades:
            print(f"testando a variabilidade: {variabilidade}")
            resposta = self.robo.get_response(variabilidade)

            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn("Olá, sou o IFBA-Bot, um robô de atendimento do IFBA, o que você gostaria de saber sobre o IFBA?".lower(), resposta.text.lower())

unittest.main()