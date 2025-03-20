from typing import Literal
from flask import Request, Response, jsonify
from app.services.auth_service import register_user, login_user

def login_view(request: Request) -> (tuple[Response, Literal[200]] | tuple[Response, Literal[401]]):
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    user = login_user(email, password)
    print(f"user: {user}")

    if not user:
        return jsonify({'message': 'Invalid credentials'}), 401
    
    return jsonify({'message': f'User {email} logged in successfully'}), 200

def register_view(request: Request) -> (tuple[Response, Literal[201]] | tuple[Response, Literal[400]]):
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    user = register_user(email, password)

    if user:
        return jsonify({'message': 'User registration failed'}), 400
    
    return jsonify({'message': 'User registered successfully'}), 201