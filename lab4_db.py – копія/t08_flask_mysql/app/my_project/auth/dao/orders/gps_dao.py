
from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain.orders.gps import Gps


class GpsDAO(GeneralDAO):
    """
    Realisation of Gps data access layer.
    """
    _domain_type = Gps

    def find_by_id(self, gps_id: int) -> Gps:

        return self._session.query(Gps).get(gps_id)

    def find_all(self):
        return Gps.query.all()
