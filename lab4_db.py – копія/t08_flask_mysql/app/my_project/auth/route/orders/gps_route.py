from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller.orders import gps_controller
from t08_flask_mysql.app.my_project.auth.domain.orders.gps import Gps


gps_bp = Blueprint('gps', __name__, url_prefix='/gps')
gps = gps_controller.GpsController()


@gps_bp.get('')
def get_all() -> Response:
    return make_response(jsonify(gps.find_all()), HTTPStatus.OK)


@gps_bp.post('')
def create() -> Response:
    content = request.get_json()
    return make_response(jsonify(gps.create(Gps.create_from_dto(content))), HTTPStatus.CREATED)


@gps_bp.get('/<int:gps_id>')
def get(gps_id: int) -> Response:
    return make_response(jsonify(gps.find_by_id(gps_id)), HTTPStatus.OK)


@gps_bp.put('/<int:gps_id>')
def update(gps_id: int) -> Response:
    content = request.get_json()
    gps.update(gps_id, Gps.create_from_dto(content))
    return make_response("Gps updated", HTTPStatus.OK)


@gps_bp.patch('/<int:gps_id>')
def patch(company_id: int) -> Response:
    content = request.get_json()
    gps.patch(company_id, content)
    return make_response("Gps updated", HTTPStatus.OK)


@gps_bp.delete('/<int:gps_id>')
def delete(gps_id: int) -> Response:
    gps.delete(gps_id)
    return make_response("Gps deleted", HTTPStatus.OK)
