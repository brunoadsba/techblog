from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://brunoadsba:8808@localhost/db_blog'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'sua_chave_secreta_jwt'

db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

from . import routes
from . import models

if __name__ == '__main__':
    app.run(debug=True)
    print("Servidor rodando em http://127.0.0.1:5000")
