import pytest
from flask import Flask, jsonify

# ==============================================================================
# DESAFIO EXTRA: API Flask[span_10](start_span)[span_10](end_span)
# ==============================================================================

app = Flask(__name__)

# Rota de teste simples
@app.route('/api/mensagem', methods=['GET'])
def obter_mensagem():
    return jsonify({"mensagem": "API Flask funcionando com sucesso!"}), 200

# Rota de verificação de status
@app.route('/api/status', methods=['GET'])
def obter_status():
    return jsonify({"status": "OK"}), 200


# ==============================================================================
# TESTES AUTOMATIZADOS COM PYTEST[span_11](start_span)[span_11](end_span)
# ==============================================================================

@pytest.fixture
def cliente():
    """Cria um cliente de testes simulado para a API Flask."""
    app.config['TESTING'] = True
    with app.test_client() as cliente_teste:
        yield cliente_teste

def test_rota_mensagem(cliente):
    """Testa a rota /api/mensagem"""
    resposta = cliente.get('/api/mensagem')
    assert resposta.status_code == 200
    assert resposta.json == {"mensagem": "API Flask funcionando com sucesso!"}

def test_rota_status(cliente):
    """Testa a rota /api/status"""
    resposta = cliente.get('/api/status')
    assert resposta.status_code == 200
    assert resposta.json == {"status": "OK"}