from flask import Blueprint
from flask_jwt_extended import jwt_required
from app.views.protected_view import protected_view

protected_bp = Blueprint('protected', __name__)

@protected_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    return protected_view()