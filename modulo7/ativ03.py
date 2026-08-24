import random
import tkinter as tk
from tkinter import messagebox


class JogoAdivinhacao:

    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Adivinhação 🎯")
        self.root.geometry("420x350")
        # 🎨 Definindo a cor de fundo da janela principal
        self.root.configure(bg="#e6f2ff")

        # Configurações do jogo
        self.limite_inferior = 1
        self.limite_superior = 24
        self.max_tentativas = 6
        self.tentativas = 0
        self.numero_secreto = random.randint(
            self.limite_inferior, self.limite_superior
        )

        # 🎯 Título principal com fonte maior e cor vibrante
        self.titulo = tk.Label(
            root,
            text="🎯 ADIVINHE O NÚMERO 🎯",
            font=("Comic Sans MS", 16, "bold"),
            bg="#e6f2ff",
            fg="#1a5276",
        )
        self.titulo.pack(pady=10)

        self.instrucao = tk.Label(
            root,
            text=f"Escolha um número entre {self.limite_inferior} e {self.limite_superior}:",
            font=("Comic Sans MS", 11),
            bg="#e6f2ff",
            fg="#2c3e50",
        )
        self.instrucao.pack(pady=5)

        # ⌨️ Caixa de entrada destacada
        self.caixa_palpite = tk.Entry(
            root, font=("Comic Sans MS", 14), justify="center", width=10
        )
        self.caixa_palpite.pack(pady=5)

        # 🔘 Botão colorido e interativo
        self.botao_chutar = tk.Button(
            root,
            text="🚀 CHUTAR!",
            command=self.verificar_palpite,
            bg="#ff5722",
            fg="white",
            font=("Comic Sans MS", 12, "bold"),
            relief="raised",
            cursor="hand2",
        )
        self.botao_chutar.pack(pady=10)

        # ⭐ Indicador visual de vidas com estrelas!
        self.label_vidas = tk.Label(
            root,
            text="⭐" * self.max_tentativas,
            font=("Arial", 16),
            bg="#e6f2ff",
            fg="#f1c40f",
        )
        self.label_vidas.pack(pady=2)

        # 📢 Mensagens de dica para o jogador
        self.status = tk.Label(
            root,
            text="Boa sorte!",
            font=("Comic Sans MS", 11, "bold"),
            bg="#e6f2ff",
            fg="#34495e",
        )
        self.status.pack(pady=5)

    def verificar_palpite(self):
        palpite = int(self.caixa_palpite.get())
        self.tentativas += 1
        restantes = self.max_tentativas - self.tentativas

        # Atualiza o contador visual de estrelas ⭐
        self.label_vidas.config(text="⭐" * restantes)

        if palpite == self.numero_secreto:
            messagebox.showinfo(
                "Vitória! 🎉",
                f"Parabéns! Você acertou em {self.tentativas} tentativa(s)!",
            )
            self.root.destroy()
        elif self.tentativas >= self.max_tentativas:
            messagebox.showwarning(
                "Fim de Jogo 💥",
                f"Suas chances acabaram! O número era {self.numero_secreto}.",
            )
            self.root.destroy()
        elif palpite < self.numero_secreto:
            self.status.config(text="📈 O número secreto é MAIOR!")
        else:
            self.status.config(text="📉 O número secreto é MENOR!")

        self.caixa_palpite.delete(0, tk.END)


if __name__ == "__main__":
    janela = tk.Tk()
    app = JogoAdivinhacao(janela)
    janela.mainloop()