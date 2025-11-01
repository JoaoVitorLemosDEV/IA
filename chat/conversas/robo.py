from chatterbot import ChatBot

NOME_ROBO = "IFBA-Bot"
CONFIANCA_MINIMA = 0.60

def configurar_robo():
    robo = ChatBot(NOME_ROBO)
    
    return robo

def executar_robo(robo):
    while True:
        mensagem = input("👤: ")
        resposta = robo.get_response(mensagem.lower())
        if resposta.confidence >= CONFIANCA_MINIMA:
            print(f"🤖: {resposta} [confianca = {resposta.confidence}]")
        else:
            print(f"🤖: Ainda não sei responder essa pergunta. Pergunte outra coisa! [confianca = {resposta.confidence}]")

if __name__ == "__main__":
    robo = configurar_robo()
    
    if robo:
        executar_robo(robo)