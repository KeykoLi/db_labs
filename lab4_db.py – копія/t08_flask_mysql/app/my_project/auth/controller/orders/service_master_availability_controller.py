from t08_flask_mysql.app.my_project.auth.service.orders import service_master_availability_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class ServiceMasterAvailabilityController(GeneralController):
    """
    Realisation of ServiceMasterAvailability controller.
    """
    _service = service_master_availability_service.ServiceMasterAvailabilityService()
