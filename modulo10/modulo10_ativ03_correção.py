import requests

chave_api = "SUA_CHAVE_API_AQUI"
cidade = input("Digite o nome da cidade: ").strip()
url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave_api}&units=metric&lang=pt_br"

try:
    # 3. Requisição com timeout de 5 segundos para prevenir conexões travadas
    resposta = requests.get(url, timeout=5)
    
    # Lança uma exceção caso o código de status seja um erro HTTP (4xx ou 5xx)
    resposta.raise_for_status()
    
    dados = resposta.json()
    print(f"\nSucesso! {dados['name']}: {dados['main']['temp']}°C, {dados['weather'][0]['description']}.")

except requests.exceptions.HTTPError as err:
    if resposta.status_code == 404:
        print("\nErro: Cidade não encontrada! Verifique se o nome está correto.")
    elif resposta.status_code == 401:
        print("\nErro: Chave de API inválida.")
    else:
        print(f"\nErro na requisição HTTP: {err}")

except requests.exceptions.Timeout:
    print("\nErro: Tempo limite excedido (Timeout)! A conexão demorou muito para responder.")

except requests.exceptions.RequestException as err:
    print(f"\nErro de rede/conexão: {err}")