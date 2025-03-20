from flask import Request
from app.models.user import User
from app.views.auth import AuthView

class AuthController:
  @staticmethod
  def register_user(request: Request) -> None | str:
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    message = User.register_user(email, password)
    return AuthView.register_view(message)
  
  @staticmethod
  def login_user(request: Request) -> User | str:
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    user = User.login_user(email, password)
    return AuthView.login_view(user)