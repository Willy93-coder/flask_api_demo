from flask import Flask
from .auth import auth_bp
from .protected import protected_bp
from .public import public_bp

def register_blueprints(app: Flask) -> None:
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(protected_bp, url_prefix='/protected')
    app.register_blueprint(public_bp, url_prefix='/public')
