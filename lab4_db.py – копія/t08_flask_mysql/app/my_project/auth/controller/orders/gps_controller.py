from t08_flask_mysql.app.my_project.auth.service.orders import gps_sevice
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class GpsController(GeneralController):
    """
    Realisation of Gps controller.
    """
    _service = gps_sevice.GpsService()
