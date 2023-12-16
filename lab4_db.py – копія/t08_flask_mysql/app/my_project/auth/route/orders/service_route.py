from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller.orders import service_controller
from t08_flask_mysql.app.my_project.auth.domain.orders.service import Service
from t08_flask_mysql.app.my_project.auth.dao import service_record_dao
from t08_flask_mysql.app.my_project.auth.domain.orders.service_and_terminal import ServiceAndTerminal
from t08_flask_mysql.app.my_project.auth.domain.orders.terminal import Terminal

service_bp = Blueprint('services', __name__, url_prefix='/services')
service = service_controller.ServiceController()



@service_bp.get('')
def get_all() -> Response:
    return make_response(jsonify(service.find_all()), HTTPStatus.OK)


@service_bp.post('')
def create() -> Response:
    content = request.get_json()
    return make_response(jsonify(service.create(Service.create_from_dto(content))), HTTPStatus.CREATED)


@service_bp.get('/<int:service_id>')
def get(service_id: int) -> Response:
    return make_response(jsonify(service.find_by_id(service_id)), HTTPStatus.OK)


@service_bp.put('/<int:service_id>')
def update(service_id: int) -> Response:
    content = request.get_json()
    service.update(service_id, Service.create_from_dto(content))
    return make_response("Service updated", HTTPStatus.OK)


@service_bp.patch('/<int:service_id>')
def patch(service_id: int) -> Response:
    content = request.get_json()
    service.patch(service_id, content)
    return make_response("Service updated", HTTPStatus.OK)


@service_bp.delete('/<int:service_id>')
def delete(service_id: int) -> Response:
    service.delete(service_id)
    return make_response("Service deleted", HTTPStatus.OK)


@service_bp.get('/<int:service_id>/service_records')
def get_available_snacks_for_product(service_id: int) -> Response:

    records = service_record_dao.find_by_service_id(service_id)
    records_dicts = [record.put_into_dto() for record in records]
    return make_response(jsonify(records_dicts), HTTPStatus.OK)


@service_bp.get('terminal')
def get_all_many() -> Response:
    array = []
    terminals = Terminal.query.all()
    for terminal in terminals:
        for service_1 in terminal.services:
            service = service_1.service
            array.append(ServiceAndTerminal(terminal.address, terminal.company_id, terminal.gps_id, terminal.installation_date, service.service_type).to_dict())
    return make_response(jsonify(array), HTTPStatus.OK)




