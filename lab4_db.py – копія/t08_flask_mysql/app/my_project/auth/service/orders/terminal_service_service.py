"""
2023
Nataliia.Parkhomchuk.IR.2022@lpnu.ua
© Nataliia Parkhomchuk
"""

from t08_flask_mysql.app.my_project.auth.dao.orders import terminal_service_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class Terminal_Service_Service(GeneralService):
    _dao = terminal_service_dao.TerminalServiceDAO()
