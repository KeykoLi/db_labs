from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain.orders.services import Service
from t08_flask_mysql.app.my_project.auth.domain.orders.service_record import ServiceRecord



class ServiceDAO(GeneralDAO):
    """
    Realisation of Person data access layer.
    """
    _domain_type = Service

    def find_by_id(self, record_id: int) -> Service:
        return self._session.query(Service).get(record_id)

    def find_all(self):
        return Service.query.all()
