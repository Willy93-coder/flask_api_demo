from flask import Blueprint, request
from app.views.auth_view import login_view, register_view

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    return login_view(request)

@auth_bp.route('/register', methods=['POST'])
def register():
    return register_view(request)