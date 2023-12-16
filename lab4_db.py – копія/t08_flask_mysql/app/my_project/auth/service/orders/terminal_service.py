"""
2023
Nataliia.Parkhomchuk.IR.2022@lpnu.ua
© Nataliia Parkhomchuk
"""

from t08_flask_mysql.app.my_project.auth.dao.orders import terminal_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class TerminalService(GeneralService):

    _dao = terminal_dao.TerminalDAO()
