from typing import Literal
from flask import Response, jsonify

class ProtectedView:
    @staticmethod
    def protected(message: str) -> (tuple[Response, Literal[200]]):
        return jsonify(message=message), 200