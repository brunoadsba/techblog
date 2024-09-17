from flask import request, jsonify
from .app import app, db
from .models import Post
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from os import environ

@app.route('/')
def home():
    return "Bem-vindo ao Tech Blog!"

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if username == environ.get('ADMIN_USERNAME') and password == environ.get('ADMIN_PASSWORD'):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
    return jsonify({"msg": "Bad username or password"}), 401

