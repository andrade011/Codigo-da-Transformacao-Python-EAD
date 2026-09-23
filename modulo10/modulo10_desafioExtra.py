import requests

# Mapeamento estático dos gêneros do TMDB para consulta rápida sem requisições extras
GENEROS_TMDB = {
    28: "Ação", 12: "Aventura", 16: "Animação", 35: "Comédia", 80: "Crime",
    99: "Documentário", 18: "Drama", 10751: "Família", 14: "Fantasia",
    36: "História", 27: "Terror", 10402: "Música", 9648: "Mistério",
    10749: "Romance", 878: "Ficção Científica", 10770: "Cinema TV",
    53: "Filme de ação", 10752: "Guerra", 37: "Faroeste"
}

def buscar_filme():
    # 1. Entrada de dados
    nome_filme = input("Digite o nome do filme: ").strip()

    # 2. Configurações da API TMDB
    chave_api = "5dfc7c8c2095938c6ed4151d7807c523" # com sua chave v3 do TMDB
    
    API_URL = "https://api.themoviedb.org/3/search/movie"

    # Parâmetros da requisição organizada em um dicionário Python
    parametros = {
        "api_key": chave_api,
        "query": nome_filme,
        "language": "pt-BR"
    }

    print("\nBuscando dados no TMDB...")

    # BLOCO 2: REQUISIÇÃO HTTP, EXTRAÇÃO E TRATAMENTO DE ERROS
    try:
        # 3. Requisição HTTP GET com tempo limite de segurança
        resposta = requests.get(API_URL, params=parametros, timeout=10)

        # Validação do Status Code (dispara HTTPError caso não seja status 200)
        resposta.raise_for_status()

        # Converta o JSON da resposta da API para um dicionário Python
        dados_filme = resposta.json()
        resultados = dados_filme.get("results", [])

        # Validação caso nenhum resultado seja retornado pela busca
        if not resultados:
            print(f"\n❌ Nenhum filme foi encontrado com o termo '{nome_filme}'.")
            return

        # Captura o primeiro filme retornado na lista de resultados
        filme = resultados[0]

        # Extração de informações do dicionário em variáveis Snake_case
        titulo_filme = filme.get("title", "Título indisponível")
        sinopse_filme = filme.get("overview", "Sinopse não informada.")
        avaliacao_filme = filme.get("vote_average", "N / D")
        ids_generos = filme.get("genre_ids", [])

        # Converta os IDs de gêneros em nomes usando o dicionário GENEROS_TMDB
        escala_generos = [GENEROS_TMDB.get(id_genero, "Outro") for id_genero in ids_generos]
        generos_formatados = ", ".join(escala_generos) if escala_generos else "Gênero não informado"

        # Exibição organizada e formatada na tela
        print("\n" + "=" * 50)
        print(f"🎬 Título: {titulo_filme}")
        print(f"🎭 Gênero(s): {generos_formatados}")
        print(f"⭐ Avaliação dos usuários: {avaliacao_filme}/10")
        print("-" * 50)
        print(f"📝 Sinopse:\n{sinopse_filme}")
        print("=" * 50)

    # TRATAMENTO DE EXCEÇÕES E ERROS DE REQUISIÇÃO HTTP
    except requests.exceptions.HTTPError as err_http:
        if resposta.status_code == 401:
            print("\n❌ Erro 401: Chave de API não autorizada ou inválida.")
        elif resposta.status_code == 404:
            print("\n❌ Erro 404: Recurso não encontrado no TMDB.")
        else:
            print(f"\n❌ Falha na requisição HTTP: {err_http}")

    except requests.exceptions.ConnectionError:
        print("\n❌ Erro de Conexão: Não foi possível conectar ao servidor do TMDB.")

    except requests.exceptions.Timeout:
        print("\n❌ Erro de Tempo Limite: O servidor do TMDB demorou para responder.")

    except requests.exceptions.RequestException as err:
        print(f"\n⚠️ Ocorreu uma falha inesperada na requisição: {err}")

# Execução principal do programa
if __name__ == "__main__":
    buscar_filme()