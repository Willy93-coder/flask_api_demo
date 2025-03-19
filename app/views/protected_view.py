from typing import Literal
from flask import Response, jsonify
from app.services.protected_service import protected_service

def protected_view() -> (tuple[Response, Literal[200]]):
    message = protected_service()
    return jsonify(message=message), 200