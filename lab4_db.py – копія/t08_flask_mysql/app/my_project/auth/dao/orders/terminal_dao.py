
from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain.orders.terminal import Terminal


class TerminalDAO(GeneralDAO):
    """
    Realisation of Terminal data access layer.
    """
    _domain_type = Terminal

    def find_by_id(self, terminal_id: int) -> Terminal:

        return self._session.query(Terminal).get(terminal_id)

    def find_all(self):
        return Terminal.query.all()
