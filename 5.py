from flask import Flask, request, jsonify

app = Flask(__name__)

cardapio = {
    101: 8.50,
    102: 4.50,
    104: 5.50,
    105: 6.60,
    106: 6.00
}

@app.route('/calcular_valor', methods=['POST'])
def calcular_valor():
    dados = request.json
    codigo = dados.get('codigo')
    quantidade = dados.get('quantidade')
    
    if codigo in cardapio:
        valor_total = cardapio[codigo] * quantidade
        return jsonify({"valor_total": valor_total})
    else:
        return jsonify({"erro": "Código do lanche inválido"}), 400

if __name__ == '__main__':
    app.run(debug=True)
