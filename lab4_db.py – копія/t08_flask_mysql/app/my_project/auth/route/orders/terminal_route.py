from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller.orders import terminal_controller
from t08_flask_mysql.app.my_project.auth.domain.orders.service import Service
from t08_flask_mysql.app.my_project.auth.domain.orders.service_and_terminal import ServiceAndTerminal
from t08_flask_mysql.app.my_project.auth.domain.orders.terminal import Terminal


terminal_bp = Blueprint('terminals', __name__, url_prefix='/terminals')
terminal = terminal_controller.TerminalController()


@terminal_bp.get('')
def get_all() -> Response:
    return make_response(jsonify(terminal.find_all()), HTTPStatus.OK)


@terminal_bp.post('')
def create() -> Response:
    content = request.get_json()
    return make_response(jsonify(terminal.create(Terminal.create_from_dto(content))), HTTPStatus.CREATED)


@terminal_bp.get('/<int:terminal_id>')
def get(terminal_id: int) -> Response:
    return make_response(jsonify(terminal.find_by_id(terminal_id)), HTTPStatus.OK)


@terminal_bp.put('/<int:terminal_id>')
def update(terminal_id: int) -> Response:
    content = request.get_json()
    terminal.update(terminal_id, Terminal.create_from_dto(content))
    return make_response("Terminal updated", HTTPStatus.OK)


@terminal_bp.patch('/<int:terminal_id>')
def patch(terminal_id: int) -> Response:
    content = request.get_json()
    terminal.patch(terminal_id, content)
    return make_response("Terminal updated", HTTPStatus.OK)


@terminal_bp.delete('/<int:terminal_id>')
def delete(terminal_id: int) -> Response:
    terminal.delete(terminal_id)
    return make_response("Terminal deleted", HTTPStatus.OK)


@terminal_bp.get('service')
def get_all_many() -> Response:
    array = []
    services = Service.query.all()
    for service in services:
        for terminal_i in service.terminals:
            terminal = terminal_i.terminal
            array.append(ServiceAndTerminal(service.service_type, terminal.address, terminal.company_id, terminal.gps_id, terminal.installation_date).to_dict())
    return make_response(jsonify(array), HTTPStatus.OK)


