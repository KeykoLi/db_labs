from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain.orders.service_master_price import ServiceMasterPrice

class ServiceMasterPriceDAO(GeneralDAO):
    """
    Realisation of ServiceMasterPrice data access layer.
    """
    _domain_type = ServiceMasterPrice

    def find_by_price(self, price: int) -> ServiceMasterPrice:
        """
        Gets ServiceMasterPrice object from the database table by field price.
        :param price: price value
        :return: ServiceMasterPrice object
        """
        return self._session.query(ServiceMasterPrice).filter(ServiceMasterPrice.price == price).order_by(ServiceMasterPrice.price).all()



    def find_all(self):
        return ServiceMasterPrice.query.all()
