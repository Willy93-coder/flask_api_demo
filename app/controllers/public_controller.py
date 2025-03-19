from flask import Blueprint
from app.views.public_view import public_view

public_bp = Blueprint('public', __name__)

@public_bp.route('/public-page', methods=['GET'])
def public():
    return public_view()