from flask import request, jsonify
from .app import app, db
from .models import User, Post
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

# Adicione um usuário administrador fixo
ADMIN_USERNAME = 'brunoadsba'
ADMIN_PASSWORD = '8808'

@app.route('/')
def home():
    return "Bem-vindo ao Tech Blog!"

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
    return jsonify({"msg": "Bad username or password"}), 401

@app.route('/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    return jsonify([post.to_dict() for post in posts])

@app.route('/admin/posts', methods=['POST'])
@jwt_required()
def create_post():
    current_user = get_jwt_identity()
    # Verifique se o usuário atual é um administrador
    if current_user != ADMIN_USERNAME:
        return jsonify({"msg": "Unauthorized"}), 403
    title = request.json.get('title', None)
    content = request.json.get('content', None)
    post = Post(title=title, content=content)
    db.session.add(post)
    db.session.commit()
    return jsonify(post.to_dict()), 201
