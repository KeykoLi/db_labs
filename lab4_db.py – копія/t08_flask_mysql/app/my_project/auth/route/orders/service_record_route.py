from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller.orders import service_record_controller
from t08_flask_mysql.app.my_project.auth.domain.orders.service_record import ServiceRecord


service_record_bp = Blueprint('service_records', __name__, url_prefix='/service_records')
service_record = service_record_controller.ServiceRecordController()


@service_record_bp.get('')
def get_all() -> Response:
    return make_response(jsonify(service_record.find_all()), HTTPStatus.OK)


@service_record_bp.post('')
def create() -> Response:
    content = request.get_json()
    return make_response(jsonify(service_record.create(ServiceRecord.create_from_dto(content))), HTTPStatus.CREATED)


@service_record_bp.get('/<int:service_record_id>')
def get(service_record_id: int) -> Response:
    return make_response(jsonify(service_record.find_by_id(service_record_id)), HTTPStatus.OK)


@service_record_bp.put('/<int:service_record_id>')
def update(service_record_id: int) -> Response:
    content = request.get_json()
    service_record.update(service_record_id, ServiceRecord.create_from_dto(content))
    return make_response("ServiceRecord updated", HTTPStatus.OK)


@service_record_bp.patch('/<int:service_record_id>')
def patch(service_record_id: int) -> Response:
    content = request.get_json()
    service_record.patch(service_record_id, content)
    return make_response("ServiceRecord updated", HTTPStatus.OK)


@service_record_bp.delete('/<int:service_record_id>')
def delete(service_record_id: int) -> Response:
    service_record.delete(service_record_id)
    return make_response("ServiceRecord deleted", HTTPStatus.OK)
