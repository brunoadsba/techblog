from flask import request, jsonify, Blueprint
from ..app import db
from ..models import Post
from flask_jwt_extended import jwt_required, get_jwt_identity
from os import environ

posts_bp = Blueprint('posts', __name__)

@posts_bp.route('', methods=['GET'])  # Rota para listar posts
def get_posts():
    posts = Post.query.all()
    return jsonify([post.to_dict() for post in posts])

@posts_bp.route('/', methods=['POST'])  # Rota para criar um novo post (admin)
@jwt_required()
def create_post():
    current_user = get_jwt_identity()
    if current_user != environ.get('ADMIN_USERNAME'):
        return jsonify({"msg": "Unauthorized"}), 403
    title = request.json.get('title', None)
    content = request.json.get('content', None)
    post = Post(title=title, content=content)
    db.session.add(post)
    db.session.commit()
    return jsonify(post.to_dict()), 201
