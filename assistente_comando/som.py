def iniciar_som():
    ...

    return True 

def atuar_sobre_som(acao, dispositivo):
    if acao in ["tocar", "parar"] and dispositivo == "som":
        print(f"Sistem de som executando a ação: {acao}")

        ...
    else:
        print(f"Sistema de som não executará esta ação")