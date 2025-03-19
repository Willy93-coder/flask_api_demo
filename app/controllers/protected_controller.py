from flask import Blueprint

protected_bp = Blueprint('protected', __name__)

@protected_bp.route('/protected', methods=['GET'])
def protected():
    return 'This is a protected page!'