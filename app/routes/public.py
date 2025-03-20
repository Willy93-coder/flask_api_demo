from flask import Blueprint
from controllers.public import PublicController

public_bp = Blueprint('public', __name__)

@public_bp.route('/public-page', methods=['GET'])
def public():
    return PublicController.public()