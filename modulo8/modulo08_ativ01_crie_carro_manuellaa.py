# ============================================================Classe Carro
# =============================================

class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        print(f"Marca: {self.marca} | Modelo: {self.modelo}")


# Teste da Atividade 1
if __name__ == "__main__":
    meu_carro = Carro("Toyota", "Corolla")
    meu_carro.exibir_info()