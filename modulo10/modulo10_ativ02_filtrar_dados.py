import requests

chave_api = "SUA_CHAVE_API_AQUI"
cidade = input("Digite o nome da cidade: ").strip()
url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave_api}&units=metric&lang=pt_br"

resposta = requests.get(url)
dados = resposta.json()

# 2. Filtrando e exibindo apenas os dados solicitados
if resposta.status_code == 200:
    nome = dados["name"]
    pais = dados["sys"]["country"]
    temp = dados["main"]["temp"]
    sensacao = dados["main"]["feels_like"]
    umidade = dados["main"]["humidity"]
    clima = dados["weather"][0]["description"].capitalize()

    print("\n" + "="*35)
    print(f"   PREVISÃO DO TEMPO: {nome} - {pais}")
    print("="*35)
    print(f" Clima:             {clima}")
    print(f" Temperatura Atual: {temp:.1f} °C")
    print(f" Sensação Térmica:  {sensacao:.1f} °C")
    print(f" Umidade do Ar:     {umidade}%")
    print("="*35)