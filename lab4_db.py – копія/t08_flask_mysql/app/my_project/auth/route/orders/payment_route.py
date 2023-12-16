from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller.orders import payment_controller
from t08_flask_mysql.app.my_project.auth.domain.orders.payment import Payment


payment_bp = Blueprint('payment', __name__, url_prefix='/payment')
payment = payment_controller.PaymentController()


@payment_bp.get('')
def get_all() -> Response:
    return make_response(jsonify(payment.find_all()), HTTPStatus.OK)


@payment_bp.post('')

def create() -> Response:
    content = request.get_json()
    return make_response(jsonify(payment.create(Payment.create_from_dto(content))), HTTPStatus.CREATED)


@payment_bp.get('/<int:payment_id>')
def get(payment_id: int) -> Response:
    return make_response(jsonify(payment.find_by_id(payment_id)), HTTPStatus.OK)


@payment_bp.put('/<int:payment_id>')
def update(payment_id: int) -> Response:
    content = request.get_json()
    payment.update(payment_id, Payment.create_from_dto(content))
    return make_response("Payment updated", HTTPStatus.OK)


@payment_bp.patch('/<int:payment_id>')
def patch(payment_id: int) -> Response:
    content = request.get_json()
    payment.patch(payment_id, content)
    return make_response("Payment updated", HTTPStatus.OK)


@payment_bp.delete('/<int:payment_id>')
def delete(payment_id: int) -> Response:
    payment.delete(payment_id)
    return make_response("Payment deleted", HTTPStatus.OK)
