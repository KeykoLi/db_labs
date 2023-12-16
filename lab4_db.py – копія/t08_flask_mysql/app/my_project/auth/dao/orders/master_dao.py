
from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain.orders.master import Master


class MasterDAO(GeneralDAO):
    """
    Realisation of Master data access layer.
    """
    _domain_type = Master

    def find_by_id(self, master_id: int) -> Master:

        return self._session.query(Master).get(master_id)

    def find_all(self):
        return Master.query.all()
