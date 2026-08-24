
import random

def jogar():
    limite_inferior = 1
    limite_superior = 24
    numero_secreto = random.randint(limite_inferior, limite_superior)
    max_tentativas = 6  # Fixamos em 6 tentativas!

    print("=" * 35)
    print("  🎯 JOGO DA ADIVINHAÇÃO SUPREMA 🎯  ")
    print("=" * 35)
    print(f"Tente acertar o número secreto entre {limite_inferior} e {limite_superior}.")
    print(f"Você tem ⏳ {max_tentativas} tentativas!\n")

    tentativas = 0
    while tentativas < max_tentativas:
        palpite = int(input(f"Tentativa {tentativas + 1}/{max_tentativas}  Digite seu palpite: "))
        tentativas += 1

        if palpite == numero_secreto:
            print(f"\n🎉 PARABÉNS! Você acertou em {tentativas} tentativa(s)! 🏆")
            break
        elif palpite < numero_secreto:
            print("📈 Dica: O número secreto é MAIOR!\n")
        else:
            print("📉 Dica: O número secreto é MENOR!\n")
    else:
        print(f"\n💥 Fim de jogo! Suas chances acabaram. O número era {numero_secreto}. 🪦")

if __name__ == "__main__":
    jogar()