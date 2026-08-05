'''
Um bloco de comentários.
Projeto hamburgueria:

PO: (como dono do negocio: quero um sistema de vendas para a minha hamburgeria,
para que eu possa controlar as vendas e produtos.)

QA: (como cliente: quero um sistema de vendas para a minha hamburgeria para 
que eu possa comprar meus produtos favoritos de forma facil e rapido.)

Tech: (como programador: quero um sistema de vendas para a minha hamburgeria,
para que eu possa desenvolver um software eficiente e funcional para o negocio.)

Dev: (como programador quero um sistema de vendas para a minha hambuergeria
 para que eu possa implementar as funcionalidades necessarias para atender as 
 necessidades do negocio e dos clientes.)

UX: (como designer de experiencia do usuario: quero um sistema de vendas
 para a minha hambuergeria para que eu possa criar uma interface intuitiva e 
 agradavel para os usuarios, garantindo uma experiencia de compra satisfatoria.)

IA: (como analista de dados: quero um sistema de vendas para a minha hamburgeria,
para que eu possa coletar e analisar os dados de vendas, ajudando a identificar
padrões de consumo e otimizar as estrategias de marketing e estoque.)
'''

import tkinter as tk
from tkinter import messagebox, ttk

# --- PALETA DE CORES PERSONALIZADA ---
COR_AZUL_ESCURO = "#004d6e"   # AE
COR_AZUL_MEDIO  = "#0081ab"   # AM
COR_AZUL_CLARO  = "#00b1cd"   # AC
COR_VERDE       = "#a6c844"   # V
COR_ROXO_VINHO  = "#b83764"   # R
COR_AMARELO     = "#edce01"   # A
COR_MARROM_DARK = "#4a3336"   # B

# --- CONFIGURAÇÃO DE DADOS MOCKADOS ---
produtos_cadastrados = [
    {"nome": "Açaí comum", "estoque": 100, "preco": 8.90, "validade": "10/12/2026", "descricao": "Açaí tradicional"}
]

cardapio_lanches = ["Hambúrguer de carne", "Hambúrguer de frango", "Hambúrguer vegetariano", "Hambúrguer vegano", "Batata frita", "Onion rings", "Salada"]
cardapio_bebidas = ["Refrigerante", "Suco natural", "Água mineral", "Cerveja"]
cardapio_sobremesas = ["Milkshake", "Sorvete", "Brownie", "Pudim"]
cardapio_combos = {
    "1": "Hambúrguer + Batata frita + Refrigerante",
    "2": "Hambúrguer + Onion rings + Suco natural",
    "3": "Hambúrguer + Salada + Água mineral"
}
combos_infantis = {
    "1": "Hambúrguer de carne + Batata frita + Refrigerante",
    "2": "Hambúrguer de frango + Onion rings + Suco natural",
    "3": "Hambúrguer vegetariano + Salada + Água mineral"
}
formas_pagamento = ["Dinheiro", "Cartão de Crédito", "Cartão de Débito", "Pix"]

# --- FUNÇÕES DE INTERAÇÃO DA INTERFACE ---

def fazer_pedido_simples(item):
    if item:
        messagebox.showinfo("Pedido Realizado", f"✅ Pedido de '{item}' realizado com sucesso!")
    else:
        messagebox.showwarning("Aviso", "Por favor, selecione um item.")

def fazer_pedido_combo(tipo_combo):
    if tipo_combo == "normal":
        combo_id = combo_normal_var.get()
        combo_desc = cardapio_combos.get(combo_id)
    else:
        combo_id = combo_infantil_var.get()
        combo_desc = combos_infantis.get(combo_id)
        
    pagam = pagamento_var.get()
    
    if not combo_id:
        messagebox.showwarning("Aviso", "Por favor, escolha um Combo!")
        return
        
    messagebox.showinfo("Pedido Confirmado", 
                        f"🎉 Pedido realizado com sucesso!\n\n"
                        f"🍔 Item: Combo {combo_id}\n"
                        f"📝 Descrição: {combo_desc}\n"
                        f"💳 Pagamento: {pagam}")

def pedir_combo_do_dia():
    pagam = pagamento_var.get()
    messagebox.showinfo("Combo do Dia", 
                        f"🔥 Pedido do Combo do Dia realizado com sucesso!\n\n"
                        f"🍔 Item: Combo 1 ({cardapio_combos['1']})\n"
                        f"💳 Pagamento: {pagam}")

def cadastrar_produto():
    nome = entry_nome.get().strip()
    try:
        estoque = int(entry_estoque.get())
        preco = float(entry_preco.get())
    except ValueError:
        messagebox.showerror("Erro", "Estoque deve ser número inteiro e Preço deve ser número decimal.")
        return
        
    validade = entry_validade.get().strip()
    desc = entry_desc.get().strip()
    
    if not nome or not validade:
        messagebox.showwarning("Aviso", "Nome e Validade são obrigatórios!")
        return
        
    novo_prod = {"nome": nome, "estoque": estoque, "preco": preco, "validade": validade, "descricao": desc}
    produtos_cadastrados.append(novo_prod)
    
    atualizar_tabela_produtos()
    
    entry_nome.delete(0, tk.END)
    entry_estoque.delete(0, tk.END)
    entry_preco.delete(0, tk.END)
    entry_validade.delete(0, tk.END)
    entry_desc.delete(0, tk.END)
    
    messagebox.showinfo("Sucesso", f"✅ Produto '{nome}' cadastrado com sucesso!")

def atualizar_tabela_produtos():
    for row in tabela.get_children():
        tabela.delete(row)
    for i, prod in enumerate(produtos_cadastrados, 1):
        tabela.insert("", tk.END, values=(i, prod['nome'], f"R$ {prod['preco']:.2f}", prod['estoque'], prod['validade']))

# --- CONSTRUÇÃO DA JANELA PRINCIPAL ---
root = tk.Tk()
root.title("Hamburgueria - Edição Especial")

# Alterado para 780x650 conforme solicitado
root.geometry("780x650")
root.configure(bg=COR_MARROM_DARK)

# Estilização de Abas e Componentes ttk
style = ttk.Style()
style.theme_use('default')
style.configure("TNotebook", background=COR_MARROM_DARK, padding=5)
style.configure("TNotebook.Tab", background=COR_AZUL_MEDIO, foreground="white", font=("Arial", 10, "bold"), padding=[10, 4])
style.map("TNotebook.Tab", background=[("selected", COR_AZUL_ESCURO)])

# Configuração da tabela
style.configure("Treeview.Heading", font=("Arial", 10, "bold"), background=COR_AZUL_ESCURO, foreground="white")
style.map("Treeview.Heading", background=[('active', COR_AZUL_MEDIO)])

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True, padx=10, pady=10)

# --- ABA 1: CARDÁPIO E PEDIDOS RÁPIDOS ---
tab1 = tk.Frame(notebook, bg=COR_AZUL_MEDIO)
notebook.add(tab1, text="🍔 Fazer Pedidos")

# Lanches
lbl_lanches = tk.Label(tab1, text="Lanches e Acompanhamentos:", bg=COR_AZUL_MEDIO, fg="white", font=("Arial", 10, "bold"))
lbl_lanches.grid(row=0, column=0, padx=15, pady=5, sticky="w")
combo_lanches = ttk.Combobox(tab1, values=cardapio_lanches, width=30, state="readonly")
combo_lanches.grid(row=1, column=0, padx=15, pady=5)
btn_pedir_lanche = tk.Button(tab1, text="Pedir Lanche", bg=COR_VERDE, fg="black", font=("Arial", 9, "bold"), command=lambda: fazer_pedido_simples(combo_lanches.get()))
btn_pedir_lanche.grid(row=1, column=1, padx=5, pady=5)

# Bebidas
lbl_bebidas = tk.Label(tab1, text="Bebidas:", bg=COR_AZUL_MEDIO, fg="white", font=("Arial", 10, "bold"))
lbl_bebidas.grid(row=2, column=0, padx=15, pady=5, sticky="w")
combo_bebidas = ttk.Combobox(tab1, values=cardapio_bebidas, width=30, state="readonly")
combo_bebidas.grid(row=3, column=0, padx=15, pady=5)
btn_pedir_bebida = tk.Button(tab1, text="Pedir Bebida", bg=COR_VERDE, fg="black", font=("Arial", 9, "bold"), command=lambda: fazer_pedido_simples(combo_bebidas.get()))
btn_pedir_bebida.grid(row=3, column=1, padx=5, pady=5)

# Sobremesas
lbl_sobremesas = tk.Label(tab1, text="Sobremesas:", bg=COR_AZUL_MEDIO, fg="white", font=("Arial", 10, "bold"))
lbl_sobremesas.grid(row=4, column=0, padx=15, pady=5, sticky="w")
combo_sobremesas = ttk.Combobox(tab1, values=cardapio_sobremesas, width=30, state="readonly")
combo_sobremesas.grid(row=5, column=0, padx=15, pady=5)
btn_pedir_sobremesa = tk.Button(tab1, text="Pedir Sobremesa", bg=COR_VERDE, fg="black", font=("Arial", 9, "bold"), command=lambda: fazer_pedido_simples(combo_sobremesas.get()))
btn_pedir_sobremesa.grid(row=5, column=1, padx=5, pady=5)

# Separador visual
canvas_sep = tk.Canvas(tab1, height=2, bg=COR_AZUL_CLARO, highlightthickness=0)
canvas_sep.grid(row=6, column=0, columnspan=3, sticky="ew", pady=15, padx=15)

# Formas de Pagamento
lbl_pagam = tk.Label(tab1, text="Forma de Pagamento para os Combos:", bg=COR_AZUL_MEDIO, fg="white", font=("Arial", 10, "bold"))
lbl_pagam.grid(row=7, column=0, padx=15, pady=5, sticky="w")
pagamento_var = tk.StringVar(value=formas_pagamento[0])
combo_pagam = ttk.Combobox(tab1, textvariable=pagamento_var, values=formas_pagamento, width=30, state="readonly")
combo_pagam.grid(row=8, column=0, padx=15, pady=5)

# Combos Normais
lbl_c_normal = tk.Label(tab1, text="Selecione um Combo:", bg=COR_AZUL_MEDIO, fg="white", font=("Arial", 10, "bold"))
lbl_c_normal.grid(row=9, column=0, padx=15, pady=5, sticky="w")
combo_normal_var = tk.StringVar()
combo_c_normal = ttk.Combobox(tab1, textvariable=combo_normal_var, values=[f"{k} - {v}" for k, v in cardapio_combos.items()], width=45, state="readonly")
combo_c_normal.grid(row=10, column=0, padx=15, pady=5)
btn_pedir_c_normal = tk.Button(tab1, text="Pedir Combo", bg=COR_AMARELO, fg="black", font=("Arial", 9, "bold"), command=lambda: fazer_pedido_combo("normal"))
btn_pedir_c_normal.grid(row=10, column=1, padx=5, pady=5)

# Combos Infantis
lbl_c_infantil = tk.Label(tab1, text="Selecione um Combo Infantil:", bg=COR_AZUL_MEDIO, fg="white", font=("Arial", 10, "bold"))
lbl_c_infantil.grid(row=11, column=0, padx=15, pady=5, sticky="w")
combo_infantil_var = tk.StringVar()
combo_c_infantil = ttk.Combobox(tab1, textvariable=combo_infantil_var, values=[f"{k} - {v}" for k, v in combos_infantis.items()], width=45, state="readonly")
combo_c_infantil.grid(row=12, column=0, padx=15, pady=5)
btn_pedir_c_infantil = tk.Button(tab1, text="Pedir Combo Infantil", bg=COR_AZUL_CLARO, fg="black", font=("Arial", 9, "bold"), command=lambda: fazer_pedido_combo("infantil"))
btn_pedir_c_infantil.grid(row=12, column=1, padx=5, pady=5)

# Combo do Dia
btn_combo_dia = tk.Button(tab1, text="🔥 PEDIR COMBO DO DIA!", bg=COR_ROXO_VINHO, fg="white", font=("Arial", 11, "bold"), command=pedir_combo_do_dia)
btn_combo_dia.grid(row=13, column=0, columnspan=2, padx=15, pady=20, sticky="ew")


# --- ABA 2: CADASTRO E LISTAGEM DE PRODUTOS ---
tab2 = tk.Frame(notebook, bg=COR_AZUL_ESCURO)
notebook.add(tab2, text="📦 Gerenciar Estoque/Produtos")

# Formulário de Entrada
frame_form = tk.LabelFrame(tab2, text=" Cadastrar Novo Produto ", bg=COR_AZUL_ESCURO, fg="white", font=("Arial", 10, "bold"))
frame_form.pack(fill="x", padx=10, pady=10)

tk.Label(frame_form, text="Nome:", bg=COR_AZUL_ESCURO, fg="white").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_nome = tk.Entry(frame_form, width=22)
entry_nome.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_form, text="Estoque:", bg=COR_AZUL_ESCURO, fg="white").grid(row=0, column=2, padx=5, pady=5, sticky="e")
entry_estoque = tk.Entry(frame_form, width=10)
entry_estoque.grid(row=0, column=3, padx=5, pady=5)

tk.Label(frame_form, text="Preço: R$", bg=COR_AZUL_ESCURO, fg="white").grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_preco = tk.Entry(frame_form, width=22)
entry_preco.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_form, text="Validade:", bg=COR_AZUL_ESCURO, fg="white").grid(row=1, column=2, padx=5, pady=5, sticky="e")
entry_validade = tk.Entry(frame_form, width=15)
entry_validade.grid(row=1, column=3, padx=5, pady=5)

tk.Label(frame_form, text="Descrição:", bg=COR_AZUL_ESCURO, fg="white").grid(row=2, column=0, padx=5, pady=5, sticky="e")
entry_desc = tk.Entry(frame_form, width=48)
entry_desc.grid(row=2, column=1, columnspan=3, padx=5, pady=5)

btn_salvar_produto = tk.Button(frame_form, text="Salvar Produto no Sistema", bg=COR_VERDE, fg="black", font=("Arial", 10, "bold"), command=cadastrar_produto)
btn_salvar_produto.grid(row=3, column=0, columnspan=4, pady=10)

# Tabela de Visualização
frame_tabela = tk.LabelFrame(tab2, text=" Produtos Cadastrados ", bg=COR_AZUL_ESCURO, fg="white", font=("Arial", 10, "bold"))
frame_tabela.pack(fill="both", expand=True, padx=10, pady=10)

colunas = ("id", "nome", "preco", "estoque", "validade")
tabela = ttk.Treeview(frame_tabela, columns=colunas, show="headings", height=10)
tabela.heading("id", text="Vaga")
tabela.heading("nome", text="Nome")
tabela.heading("preco", text="Preço")
tabela.heading("estoque", text="Em Estoque")
tabela.heading("validade", text="Validade")

tabela.column("id", width=50, anchor="center")
tabela.column("nome", width=180)
tabela.column("preco", width=90, anchor="center")
tabela.column("estoque", width=90, anchor="center")
tabela.column("validade", width=110, anchor="center")

tabela.pack(fill="both", expand=True, padx=5, pady=5)

# Carregar o estado inicial na tabela
atualizar_tabela_produtos()

root.mainloop()