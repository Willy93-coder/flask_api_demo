from typing import Literal
from flask import Response, jsonify

class PublicView:
    @staticmethod
    def public(message: str) -> (tuple[Response, Literal[200]]):
        return jsonify(message=message), 200