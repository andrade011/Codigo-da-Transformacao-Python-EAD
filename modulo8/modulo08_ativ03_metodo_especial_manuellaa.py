# ============================================================
# Métodos Especiais (__init__ e __str__)
# =================================================

class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    # Método especial __str__ para personalizar a exibição em texto
    def __str__(self):
        return f"Veículo: {self.marca} {self.modelo}"


# Teste da Atividade 3
if __name__ == "__main__":
    carro1 = Carro("Honda", "Civic")
    print(carro1)  # Ao usar print(), o Python chama automaticamente o método __str__