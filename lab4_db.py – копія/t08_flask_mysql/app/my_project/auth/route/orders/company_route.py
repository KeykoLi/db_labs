from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller.orders import company_controller
from t08_flask_mysql.app.my_project.auth.domain.orders.company import Company


company_bp = Blueprint('companies', __name__, url_prefix='/companies')
company = company_controller.CompanyController()


@company_bp.get('')
def get_all_companies() -> Response:
    return make_response(jsonify(company.find_all()), HTTPStatus.OK)


@company_bp.post('')
def create_company() -> Response:
    content = request.get_json()
    return make_response(jsonify(company.create(Company.create_from_dto(content))), HTTPStatus.CREATED)


@company_bp.get('/<int:company_id>')
def get_company(company_id: int) -> Response:
    return make_response(jsonify(company.find_by_id(company_id)), HTTPStatus.OK)


@company_bp.put('/<int:company_id>')
def update_company(company_id: int) -> Response:
    content = request.get_json()
    company.update(company_id, Company.create_from_dto(content))
    return make_response("Company updated", HTTPStatus.OK)


@company_bp.patch('/<int:company_id>')
def patch_company(company_id: int) -> Response:
    content = request.get_json()
    company.patch(company_id, content)
    return make_response("Company updated", HTTPStatus.OK)


@company_bp.delete('/<int:company_id>')
def delete_company(company_id: int) -> Response:
    company.delete(company_id)
    return make_response("Company deleted", HTTPStatus.OK)
