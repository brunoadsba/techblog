from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from os import environ

load_dotenv()  # Carrega as variáveis do arquivo .env

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://brunoadsba:8808@localhost/db_blog'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = environ.get('JWT_SECRET_KEY')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

CORS(app)

# Configuração de codificação UTF-8
app.config['JSON_AS_ASCII'] = False

from . import routes
from . import models

if __name__ == '__main__':
        app.run(host='0.0.0.0', debug=True)
        print("Servidor rodando em http://127.0.0.1:5000")
