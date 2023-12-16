from typing import List

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain.orders.company import Company


class CompanyDAO(GeneralDAO):
    """
    Realisation of Company data access layer.
    """
    _domain_type = Company

    def find_by_name(self, name: str) -> List[Company]:
        """
        Gets Company objects from the database table by field name.
        :param name: name value
        :return: list of Company objects
        """
        return self._session.query(Company).filter(Company.name == name).order_by(Company.name).first()

    def find_by_address(self, company_address: str) -> List[Company]:
        """
        Gets Company objects from the database table by field company address.
        :param company_address: company_address value
        :return: list of Company objects
        """
        return self._session.query(Company).filter(Company.company_addres == company_address).first()

    def find_by_id(self, company_id: int) -> Company:
        """
        Gets Company object from the database table by ID.
        :param company_id: ID of the companys
        :return: Company object
        """
        return self._session.query(Company).get(company_id)

    def find_all(self):
        return Company.query.all()
