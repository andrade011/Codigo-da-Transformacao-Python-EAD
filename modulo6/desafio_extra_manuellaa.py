
import os
import shutil

# Definindo pasta de origem e pasta de destino (backup)
pasta_origem = "dados_importantes"
pasta_backup = "pasta_backup"

# Cria a pasta de origem para teste (caso não exista) e um arquivo
os.makedirs(pasta_origem, exist_ok=True)
with open(os.path.join(pasta_origem, "relatorio.txt"), "w", encoding="utf-8") as f:
    f.write("Este é um relatório importante para o backup.")

# --- Realizando o Backup usando shutil ---
if os.path.exists(pasta_origem):
    # Copia toda a pasta e seu conteúdo para a pasta de backup
    shutil.copytree(pasta_origem, pasta_backup, dirs_exist_ok=True)
    print(f"✅ Backup realizado com sucesso de '{pasta_origem}' para '{pasta_backup}'!")
else:
    print("❌ Pasta de origem não encontrada.")