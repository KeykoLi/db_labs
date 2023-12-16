
from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain.orders.service_record import ServiceRecord


class ServiceRecordDAO(GeneralDAO):
    """
    Realisation of ServiceRecord data access layer.
    """
    _domain_type = ServiceRecord

    def find_by_id(self, record_id: int) -> ServiceRecord:

        return self._session.query(ServiceRecord).get(record_id)

    def find_all(self):
        return ServiceRecord.query.all()

    def find_by_service_id(self, service_id: int):
        return self._session.query(ServiceRecord).filter(ServiceRecord.service_id == service_id).all()
