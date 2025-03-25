from typing import Literal
from flask import Request, Response
from app.models.user import User
from app.views.auth import AuthView

class AuthController:
  @staticmethod
  def register_user(request: Request) -> (tuple[Response, Literal[201]] | tuple[Response, Literal[400]]):
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    message = User.register_user(email, password)
    return AuthView.register_view(message)
  
  @staticmethod
  def login_user(request: Request) -> (tuple[Response, Literal[200]] | tuple[Response, Literal[401]]):
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    user = User.login_user(email, password)
    return AuthView.login_view(user)