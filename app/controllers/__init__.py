from flask import Flask
from .auth_controller import auth_bp

def register_blueprints(app: Flask) -> None:
    app.register_blueprint(auth_bp, url_prefix='/auth')
