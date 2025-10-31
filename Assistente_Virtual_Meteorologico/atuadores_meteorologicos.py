import requests

API_KEY = "KEY_DA_SUA_API_AQUI"
CIDADE = "Vitória da Conquista,BR"

def iniciar_meteorologia():
    print("Assistente meteorológico iniciado")
    return True

def atuar_sobre_clima(acao, dispositivo):
    if acao == "mostrar_previsao":
        previsao = obter_previsao()
        print(f"Previsão para hoje: {previsao}")
    elif acao == "vai_chover":
        chuva = verificar_chuva_amanha()
        print(f"Vai chover amanhã? {'Sim' if chuva else 'Não'}")
    elif acao == "temperatura_atual":
        temp, sensacao = obter_temperatura_atual()
        print(f"Temperatura atual: {temp}°C, sensação térmica: {sensacao}°C")
    elif acao == "atualizar_dados":
        atualizar_dados()
        print("Dados meteorológicos atualizados")
    else:
        print("Ação não reconhecida")

def obter_previsao():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CIDADE}&appid={API_KEY}&units=metric&lang=pt_br"
    resp = requests.get(url).json()
    return resp.get("weather", [{}])[0].get("description", "Indisponível")

def verificar_chuva_amanha():
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={CIDADE}&appid={API_KEY}&units=metric&lang=pt_br"
    resp = requests.get(url).json()
    for bloco in resp.get("list", [])[:8]:
        if "rain" in bloco:
            return True
    return False

def obter_temperatura_atual():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CIDADE}&appid={API_KEY}&units=metric&lang=pt_br"
    resp = requests.get(url).json()
    temp = resp.get("main", {}).get("temp", 0)
    sensacao = resp.get("main", {}).get("feels_like", 0)
    return temp, sensacao

import requests

def atualizar_dados():
    """Atualiza os dados meteorológicos em cache."""
    url_atual = f"http://api.openweathermap.org/data/2.5/weather?q={CIDADE}&appid={API_KEY}&units=metric&lang=pt_br"
    url_previsao = f"http://api.openweathermap.org/data/2.5/forecast?q={CIDADE}&appid={API_KEY}&units=metric&lang=pt_br"

    try:
        dados_atuais = requests.get(url_atual).json()

        dados_previsao = requests.get(url_previsao).json()

        global cache_dados_atuais, cache_dados_previsao
        cache_dados_atuais = dados_atuais
        cache_dados_previsao = dados_previsao

        print("Dados meteorológicos atualizados com sucesso!")

    except Exception as e:
        print(f"Erro ao atualizar dados: {str(e)}")

