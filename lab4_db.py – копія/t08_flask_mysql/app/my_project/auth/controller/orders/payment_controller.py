from t08_flask_mysql.app.my_project.auth.service.orders import payment_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class PaymentController(GeneralController):
    """
    Realisation of Payment controller.
    """
    _service = payment_service.PaymentService()
