# ==============================================================================
# 🎯 Projeto: Sistema de Validação de Login
# ==============================================================================

# 📄 Passo 1: Base de dados (Dicionário com 'usuario': 'senha')
banco_de_usuarios = {
    "admin": "1234",
    "maria": "python2026",
    "joao": "seguranca123"
}

# 📄 Passo 2: Definir a função de validação
def validar_login(usuario_digitado, senha_digitada):
    # 1. Verifica se o usuário existe nas chaves do dicionário
    if usuario_digitado in banco_de_usuarios:
        # 2. Se o usuário existe, confere se a senha corresponde ao valor associado
        if banco_de_usuarios[usuario_digitado] == senha_digitada:
            return "✅ Login realizado com sucesso! Bem-vindo ao sistema."
        else:
            return "❌ Senha incorreta."
    else:
        return "❌ Usuário não encontrado."


# ==============================================================================
# 🔹 Passo 3: Executar a interatividade com o usuário

print("--- 🔐 TELA DE LOGIN ---")
user = input("Digite seu nome de usuário: ")
password = input("Digite sua senha: ")

# Chamada da função passando os dados informados
resultado_autenticacao = validar_login(user, password)
print(resultado_autenticacao)