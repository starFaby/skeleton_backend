from flask import Blueprint
from flask import Blueprint
from app.controller.controllerUser import onGetCreateUser
user_bp = Blueprint('user_bp', __name__)
user_bp.route('/user_bp', methods=['GET'])(onGetCreateUser)
# user_bp.route('/create', methods=['POST'])(store)
# user_bp.route('/<int:user_id>', methods=['GET'])(show)
# user_bp.route('/<int:user_id>/edit', methods=['POST'])(update)
# user_bp.route('/<int:user_id>', methods=['DELETE'])(destroy)
