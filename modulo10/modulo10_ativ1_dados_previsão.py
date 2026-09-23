import requests

# Configuração dos parâmetros de acesso
chave_api = "SUA_CHAVE_API_AQUI"  # Substitua pela sua chave da OpenWeatherMap
cidade = "São Paulo"
url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave_api}&units=metric&lang=pt_br"

# 1. Fazendo a requisição à API
resposta = requests.get(url)

# Exibindo o código de status e a resposta bruta em JSON
print("Status da Requisição:", resposta.status_code)
print("Dados em formato JSON:", resposta.json())