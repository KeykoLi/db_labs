from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller.orders.service_master_availability_controller import ServiceMasterAvailabilityController
from t08_flask_mysql.app.my_project.auth.domain.orders.service_master_availability import ServiceMasterAvailability

service_master_availability_bp = Blueprint('service_master_availability', __name__, url_prefix='/service_master_availability')
service_master_availability = ServiceMasterAvailabilityController()


@service_master_availability_bp.get('')
def get_all_availability() -> Response:

    return make_response(jsonify(service_master_availability.find_all()), HTTPStatus.OK)


@service_master_availability_bp.post('')
def create_availabilitys() -> Response:

    content = request.get_json()
    return make_response(jsonify(service_master_availability.create(ServiceMasterAvailability.create_from_dto(content))), HTTPStatus.CREATED)


@service_master_availability_bp.get('/<int:availability_id>')
def get_availability(availability_id: int) -> Response:

    return make_response(jsonify(service_master_availability.find_by_id(availability_id)), HTTPStatus.OK)


@service_master_availability_bp.put('/<int:availability_id>')
def update_availability(availability_id: int) -> Response:

    service_master_availability.update(availability_id, ServiceMasterAvailability.create_from_dto(request.get_json()))
    return make_response("Availability updated", HTTPStatus.OK)


@service_master_availability_bp.patch('/<int:availability_id>')
def patch_availability(availability_id: int) -> Response:

    service_master_availability.patch(availability_id, request.get_json())
    return make_response("Availability updated", HTTPStatus.OK)


@service_master_availability_bp.delete('/<int:availability_id>')
def delete_availability(availability_id: int) -> Response:

    service_master_availability.delete(availability_id)
    return make_response("Availability deleted", HTTPStatus.OK)
