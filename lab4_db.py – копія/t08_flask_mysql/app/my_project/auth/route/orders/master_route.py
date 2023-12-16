from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller.orders import master_controller
from t08_flask_mysql.app.my_project.auth.domain.orders.master import Master


master_bp = Blueprint('masters', __name__, url_prefix='/masters')
master = master_controller.MasterController()


@master_bp.get('')
def get_all() -> Response:
    return make_response(jsonify(master.find_all()), HTTPStatus.OK)


@master_bp.post('')

def create() -> Response:
    content = request.get_json()
    return make_response(jsonify(master.create(Master.create_from_dto(content))), HTTPStatus.CREATED)


@master_bp.get('/<int:master_id>')
def get(master_id: int) -> Response:
    return make_response(jsonify(master.find_by_id(master_id)), HTTPStatus.OK)


@master_bp.put('/<int:master_id>')
def update(master_id: int) -> Response:
    content = request.get_json()
    master.update(master_id, Master.create_from_dto(content))
    return make_response("Master updated", HTTPStatus.OK)


@master_bp.patch('/<int:master_id>')
def patch(master_id: int) -> Response:
    content = request.get_json()
    master.patch(master_id, content)
    return make_response("Master updated", HTTPStatus.OK)


@master_bp.delete('/<int:master_id>')
def delete(master_id: int) -> Response:
    master.delete(master_id)
    return make_response("Master deleted", HTTPStatus.OK)
