from t08_flask_mysql.app.my_project.auth.service.orders import service_master_price_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class ServiceMasterPriceController(GeneralController):
    """
    Realisation of ServiceMasterPrice controller.
    """
    _service = service_master_price_service.ServiceMasterPriceService()
