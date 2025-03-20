from typing import Literal
from flask import Response, jsonify
from app.models.user import User

class AuthView:
    @staticmethod
    def login_view(user: User | None) -> (tuple[Response, Literal[200]] | tuple[Response, Literal[401]]):
        if not user:
            return jsonify({'message': 'Invalid credentials'}), 401
        
        return jsonify({'message': f'User {user.email} logged in successfully'}), 200

    @staticmethod
    def register_view(message: str | None) -> (tuple[Response, Literal[201]] | tuple[Response, Literal[400]]):
        if message:
            return jsonify({'message': message}), 400
        
        return jsonify({'message': 'User registered successfully'}), 201