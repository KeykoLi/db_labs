from t08_flask_mysql.app.my_project.auth.service.orders import company_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class CompanyController(GeneralController):
    """
    Realisation of Companycontroller.
    """
    _service = company_service.CompanyService()
