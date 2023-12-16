"""
2023
Nataliia.Parkhomchuk.IR.2022@lpnu.ua
© Nataliia Parkhomchuk
"""

from t08_flask_mysql.app.my_project.auth.dao.orders import service_record_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class ServiceRecordService(GeneralService):

    _dao = service_record_dao.ServiceRecordDAO()
