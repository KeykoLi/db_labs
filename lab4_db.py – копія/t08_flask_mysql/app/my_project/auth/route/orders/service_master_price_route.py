from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller.orders import service_master_price_controller
from t08_flask_mysql.app.my_project.auth.domain.orders.service_master_price import ServiceMasterPrice


price_bp = Blueprint('price', __name__, url_prefix='/price')
price = service_master_price_controller.ServiceMasterPriceController()


@price_bp.get('')
def get_all() -> Response:
    return make_response(jsonify(price.find_all()), HTTPStatus.OK)


@price_bp.post('')

def create() -> Response:
    content = request.get_json()
    return make_response(jsonify(price.create(ServiceMasterPrice.create_from_dto(content))), HTTPStatus.CREATED)


@price_bp.get('/<int:price_id>')
def get(price_id: int) -> Response:
    return make_response(jsonify(price.find_by_id(price_id)), HTTPStatus.OK)


@price_bp.put('/<int:price_id>')
def update(price_id: int) -> Response:
    content = request.get_json()
    price.update(price_id, ServiceMasterPrice.create_from_dto(content))
    return make_response("ServiceMasterPrice updated", HTTPStatus.OK)


@price_bp.patch('/<int:price_id>')
def patch(price_id: int) -> Response:
    content = request.get_json()
    price.patch(price_id, content)
    return make_response("ServiceMasterPrice updated", HTTPStatus.OK)


@price_bp.delete('/<int:price_id>')
def delete(payment_id: int) -> Response:
    price.delete(payment_id)
    return make_response("ServiceMasterPrice deleted", HTTPStatus.OK)
