from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from os import environ
from .posts import posts_bp

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Cria a aplicação Flask
app = Flask(__name__)

# Registra o blueprint
app.register_blueprint(posts_bp, url_prefix='/posts')

