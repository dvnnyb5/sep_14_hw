from flask import Blueprint

from controllers import user_controller

user = Blueprint('user', __name__)


@user.route('/user', methods=['POST'])
def user_add():
    return user_controller.user_add()


@user.route('/user/<user_id>', methods=['GET'])
def user_get_by_id(user_id):
    return user_controller.user_get_by_id(user_id)


@user.route('/users', methods=['GET'])
def users_get_all():
    return user_controller.users_get_all()


@user.route('/user/<user_id>', methods=['PATCH'])
def user_activity(user_id):
    return user_controller.user_activity(user_id)


@user.route('/user/<user_id>', methods=['DELETE'])
def user_delete_by_id(user_id):
    return user_controller.user_delete_by_id(user_id)


@user.route('/user/<user_id>', methods=["PUT"])
def user_update_by_id(user_id):
    return user_controller.user_update_by_id(user_id)