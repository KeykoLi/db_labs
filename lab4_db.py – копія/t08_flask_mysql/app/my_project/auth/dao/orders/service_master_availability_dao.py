
from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain.orders.service_master_availability import ServiceMasterAvailability


class ServiceMasterAvailabilityDAO(GeneralDAO):
    """
    Realisation of ServiceMasterAvailability data access layer.
    """
    _domain_type = ServiceMasterAvailability

    def find_by_id(self, availability_id: int) -> ServiceMasterAvailability:

        return self._session.query(ServiceMasterAvailability).get(availability_id)

    def find_all(self):
        return ServiceMasterAvailability.query.all()
