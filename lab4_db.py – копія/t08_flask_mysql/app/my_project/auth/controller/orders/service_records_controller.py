from t08_flask_mysql.app.my_project.auth.service.orders import service_record_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class ServiceRecordController(GeneralController):


    _service = service_record_service.ServiceRecordService()
