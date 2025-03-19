from typing import Literal
from flask import Response, jsonify
from app.services.public_service import public_service

def public_view() -> (tuple[Response, Literal[200]]):
    message = public_service()
    return jsonify(message=message), 200