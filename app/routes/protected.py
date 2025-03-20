from flask import Blueprint
from flask_jwt_extended import jwt_required
from controllers.protected import ProtectedController

protected_bp = Blueprint('protected', __name__)

@protected_bp.route('/protected-page', methods=['GET'])
@jwt_required()
def protected():
    return ProtectedController.protected_page()