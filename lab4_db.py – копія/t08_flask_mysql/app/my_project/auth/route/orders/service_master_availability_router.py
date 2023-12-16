from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller.orders import service_master_availability_controller
from t08_flask_mysql.app.my_project.auth.domain.orders.service_master_availability import ServiceMasterAvailability


availability_bp = Blueprint('availability', __name__, url_prefix='/availability')
availability = service_master_availability_controller.ServiceMasterAvailabilityController()


@availability_bp.get('')
def get_all() -> Response:
    return make_response(jsonify(availability.find_all()), HTTPStatus.OK)


@availability_bp.post('')

def create() -> Response:
    content = request.get_json()
    return make_response(jsonify(availability.create(ServiceMasterAvailability.create_from_dto(content))), HTTPStatus.CREATED)


@availability_bp.get('/<int:availability_id>')
def get(availability_id: int) -> Response:
    return make_response(jsonify(availability.find_by_id(availability_id)), HTTPStatus.OK)


@availability_bp.put('/<int:availability_id>')
def update(availability_id: int) -> Response:
    content = request.get_json()
    availability.update(availability_id, ServiceMasterAvailability.create_from_dto(content))
    return make_response("ServiceMasterAvailability updated", HTTPStatus.OK)


@availability_bp.patch('/<int:availability_id>')
def patch(availability_id: int) -> Response:
    content = request.get_json()
    availability.patch(availability_id, content)
    return make_response("ServiceMasterAvailability updated", HTTPStatus.OK)


@availability_bp.delete('/<int:availability_id>')
def delete(availability_id: int) -> Response:
    availability.delete(availability_id)
    return make_response("ServiceMasterAvailability deleted", HTTPStatus.OK)
