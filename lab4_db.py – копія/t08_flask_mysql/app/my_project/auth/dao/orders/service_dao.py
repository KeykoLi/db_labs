
from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain.orders.service import Service


class ServiceDAO(GeneralDAO):
    """
    Realisation of Service data access layer.
    """
    _domain_type = Service

    def find_by_id(self, service_id: int) -> Service:

        return self._session.query(Service).get(service_id)

    def find_all(self):
        return Service.query.all()
