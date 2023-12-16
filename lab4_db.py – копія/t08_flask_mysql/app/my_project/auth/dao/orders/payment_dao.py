
from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain.orders.payment import Payment


class PaymentDAO(GeneralDAO):
    """
    Realisation of Payment data access layer.
    """
    _domain_type = Payment

    def find_by_id(self, payment_id: int) -> Payment:

        return self._session.query(Payment).get(payment_id)

    def find_all(self):
        return Payment.query.all()
