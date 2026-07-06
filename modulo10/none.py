print("Olá, Mundo! Este é um teste do comando print().")

# 2. Utilizando o comando type() para identificar tipos de dados
texto = "Vocação"
numero_inteiro = 10
numero_decimal = 5.7
booleano = True

print("\nIdentificando os tipos de dados com type():")
print(f"O tipo de '{texto}' é:", type(texto))
print(f"O tipo de {numero_inteiro} é:", type(numero_inteiro))
print(f"O tipo de {numero_decimal} é:", type(numero_decimal))
print(f"O tipo de {booleano} é:", type(booleano))

# 3. Extra: Usando o comando len() para ver a quantidade de caracteres
print("\nComprimento da palavra 'Vocação' com len():", len(texto))





nome = input("Por favor, digite o seu nome: ")

# Exibe a saudação personalizada
print(f"Olá, {nome}! Seja muito bem-vindo(a) ao mundo da programação com Python!")




nome = input("Por favor, digite o seu nome: ")

# Obtém o horário atual do sistema
agora = datetime.now()

# Formata a hora para o padrão brasileiro (Hora:Minuto)
hora_formatada = agora.strftime("%H:%M")

# Exibe a mensagem final com a saudação e o horário atual
print(f"Olá, {nome}! Muito bem-vindo(a)! Agora são {hora_formatada}.")