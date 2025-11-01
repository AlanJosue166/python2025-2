
from flask import Flask
from cliente import cliente 

app = Flask(__name__)
app.register_blueprint(cliente)

@app.route('/')
def home():
    return "Servicio de clientes activo"
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5003)