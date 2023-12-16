"""
2023
Nataliia.Parkhomchuk.IR.2022@lpnu.ua
© Nataliia Parkhomchuk
"""

from t08_flask_mysql.app.my_project.auth.dao.orders import master_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class MasterService(GeneralService):

    _dao = master_dao.MasterDAO()
