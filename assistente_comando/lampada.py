def iniciar_lampada():
    ...

    return True

def atuar_sobre_lampada(acao, dispositivo):
    if acao in ["ligar", "acender", "desligar", "apagar"] and dispositivo == "lâmpada":
        print(f"Lâmpada executando a ação: {acao}")

        ...
    else:
        print(f"Lâmpada não executando esta ação")
        
