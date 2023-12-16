from t08_flask_mysql.app.my_project.auth.service.orders import services_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class ServiceController(GeneralController):


    _service = services_service.ServiceService()
