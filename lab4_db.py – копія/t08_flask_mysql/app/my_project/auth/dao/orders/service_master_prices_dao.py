
from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain.orders.service_master_price import ServiceMasterPrice


class ServiceMasterPriceDAO(GeneralDAO):
    """
    Realisation of ServiceMasterPrice data access layer.
    """
    _domain_type = ServiceMasterPrice

    def find_by_id(self, price_id: int) -> ServiceMasterPrice:

        return self._session.query(ServiceMasterPrice).get(price_id)

    def find_all(self):
        return ServiceMasterPrice.query.all()
