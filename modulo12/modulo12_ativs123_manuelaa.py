import unittest

# ==============================================================================
# CÓDIGO A SER TESTADO (Função e Classe Calculadora)
# ==============================================================================

# Atividade 1: Função de soma simples[span_3](start_span)[span_3](end_span)
def somar(a, b):
    return a + b

# Atividade 2: Classe Calculadora com operações matemáticas[span_4](start_span)[span_4](end_span)
class Calculadora:
    def somar(self, a, b):
        return a + b

    def subtrair(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        # Atividade 3: Lança exceção ao tentar dividir por zero[span_5](start_span)[span_5](end_span)
        if b == 0:
            raise ValueError("Não é possível dividir por zero!")
        return a / b


# ==============================================================================
# TESTES AUTOMATIZADOS USANDO UNITTEST
# ==============================================================================

class TestesModulo12(unittest.TestCase):

    # --------------------------------------------------------------------------
    # ATIVIDADE 1: Teste de uma função de soma simples[span_6](start_span)[span_6](end_span)
    # --------------------------------------------------------------------------
    def test_funcao_somar(self):
        resultado = somar(2, 3)
        self.assertEqual(resultado, 5)

    # --------------------------------------------------------------------------
    # ATIVIDADE 2: Testes para a classe Calculadora[span_7](start_span)[span_7](end_span)
    # --------------------------------------------------------------------------
    def setUp(self):
        """Método executado antes de cada teste para instanciar a calculadora."""
        self.calc = Calculadora()

    def test_metodo_somar(self):
        self.assertEqual(self.calc.somar(10, 5), 15)

    def test_metodo_subtrair(self):
        self.assertEqual(self.calc.subtrair(10, 5), 5)

    def test_metodo_multiplicar(self):
        self.assertEqual(self.calc.multiplicar(4, 3), 12)

    def test_metodo_dividir(self):
        self.assertEqual(self.calc.dividir(10, 2), 5.0)

    # --------------------------------------------------------------------------
    # ATIVIDADE 3: Validação de entradas inválidas (Divisão por zero)[span_8](start_span)[span_8](end_span)
    # --------------------------------------------------------------------------
    def test_divisao_por_zero(self):
        # Verifica se o método lança a exceção ValueError ao passar zero no divisor
        with self.assertRaises(ValueError):
            self.calc.dividir(10, 0)


# ==============================================================================
# EXECUÇÃO DOS TESTES
# ==============================================================================
if __name__ == '__main__':
    unittest.main()