from flask import Flask
from routes import worker_routes

app = Flask(__name__)

# Configuração das rotas
app.register_blueprint(worker_routes)

if __name__ == '__main__':
    app.run(debug=True)
