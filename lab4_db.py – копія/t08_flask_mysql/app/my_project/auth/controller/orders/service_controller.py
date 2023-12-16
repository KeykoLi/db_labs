from t08_flask_mysql.app.my_project.auth.service.orders import service_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class ServiceController(GeneralController):
    """
    Realisation of Service controller.
    """
    _service = service_service.ServiceService()
