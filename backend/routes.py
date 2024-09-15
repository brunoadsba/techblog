from flask import request, jsonify
from .app import app, db
from .models import User, Post
from flask_jwt_extended import create_access_token, jwt_required
from werkzeug.security import generate_password_hash, check_password_hash

@app.route('/')
def home():
    return "Bem-vindo ao Tech Blog!"

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and check_password_hash(user.password, data['password']):
        access_token = create_access_token(identity={'username': user.username})
        return jsonify(access_token=access_token), 200
    return jsonify({"msg": "Nome de usuário ou senha incorretos"}), 401

@app.route('/posts', methods=['GET'])
@jwt_required()
def get_posts():
    posts = Post.query.all()
    return jsonify([{'id': post.id, 'title': post.title, 'content': post.content} for post in posts])

@app.route('/posts', methods=['POST'])
@jwt_required()
def create_post():
    data = request.get_json()
    new_post = Post(title=data['title'], content=data['content'])
    db.session.add(new_post)
    db.session.commit()
    return jsonify({'id': new_post.id, 'title': new_post.title, 'content': new_post.content}), 201
