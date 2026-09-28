from django.db import models
from django.urls import path
from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import redirect, get_object_or_404
from django.contrib import admin
from django.test import TestCase

# ==============================================================================
# ATIVIDADE 1: Modelo de Produto
# ==============================================================================

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField()

    def __str__(self):
        return self.nome


# ==============================================================================
# ATIVIDADE 3: Configuração do Painel de Administração
# ==============================================================================

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'quantidade')
    search_fields = ('nome',)


# ==============================================================================
# ATIVIDADE 2: Views CRUD com HTML Embutido no mesmo arquivo
# ==============================================================================

# HTML incorporado em variável de texto
HTML_LISTAR = '''
<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <title>Lista de Produtos</title>
</head>
<body>
    <h1>Produtos Cadastrados</h1>
    <table border="1">
        <tr>
            <th>Nome</th>
            <th>Descrição</th>
            <th>Preço</th>
            <th>Quantidade</th>
        </tr>
        {% for produto in produtos %}
        <tr>
            <td>{{ produto.nome }}</td>
            <td>{{ produto.descricao }}</td>
            <td>R$ {{ produto.preco }}</td>
            <td>{{ produto.quantidade }}</td>
        </tr>
        {% empty %}
        <tr>
            <td colspan="4">Nenhum produto cadastrado.</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
'''

def listar_produtos(request):
    """View que busca os produtos e renderiza o HTML embutido."""
    produtos = Produto.objects.all()
    template = Template(HTML_LISTAR)
    contexto = Context({'produtos': produtos})
    return HttpResponse(template.render(contexto))

def cadastrar_produto(request):
    """View para cadastro simples via POST."""
    if request.method == 'POST':
        Produto.objects.create(
            nome=request.POST.get('nome'),
            descricao=request.POST.get('descricao'),
            preco=request.POST.get('preco'),
            quantidade=request.POST.get('quantidade')
        )
        return redirect('listar_produtos')
    return HttpResponse("Envie os dados do produto via método POST.")

def atualizar_produto(request, pk):
    """View para atualização simples."""
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        produto.nome = request.POST.get('nome', produto.nome)
        produto.save()
        return redirect('listar_produtos')
    return HttpResponse(f"Atualizando produto: {produto.nome}")

def excluir_produto(request, pk):
    """View para exclusão simples."""
    produto = get_object_or_404(Produto, pk=pk)
    produto.delete()
    return redirect('listar_produtos')


# Mapeamento de Rotas
urlpatterns = [
    path('', listar_produtos, name='listar_produtos'),
    path('cadastrar/', cadastrar_produto, name='cadastrar_produto'),
    path('atualizar/<int:pk>/', atualizar_produto, name='atualizar_produto'),
    path('excluir/<int:pk>/', excluir_produto, name='excluir_produto'),
]


# ==============================================================================
# ATIVIDADE 3: Testes Automatizados
# ==============================================================================

class ProdutoModelTest(TestCase):
    def setUp(self):
        self.produto = Produto.objects.create(
            nome="Mouse Gamer",
            descricao="Mouse RGB 10000 DPI",
            preco=150.00,
            quantidade=5
        )

    def test_criacao_produto(self):
        self.assertEqual(self.produto.nome, "Mouse Gamer")
        self.assertEqual(self.produto.quantidade, 5)