from t08_flask_mysql.app.my_project.auth.service.orders import terminal_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class TerminalController(GeneralController):
    """
    Realisation of Terminal controller.
    """
    _service = terminal_service.TerminalService()
