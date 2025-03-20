from flask import Blueprint, request
from controllers.auth import AuthController

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    return AuthController.login_user(request)

@auth_bp.route('/register', methods=['POST'])
def register():
    return AuthController.register_user(request)