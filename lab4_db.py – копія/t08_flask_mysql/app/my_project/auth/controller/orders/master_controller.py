from t08_flask_mysql.app.my_project.auth.service.orders import master_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class MasterController(GeneralController):
    """
    Realisation of Master controller.
    """
    _service = master_service.MasterService()
