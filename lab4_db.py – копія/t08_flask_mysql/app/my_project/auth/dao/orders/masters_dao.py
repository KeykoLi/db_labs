from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain.orders.masters import Master


class MasterDAO(GeneralDAO):
    """
    Realisation of Master data access layer.
    """
    _domain_type = Master

    def find_by_name(self, name: str) -> Master:
        """
        Gets Master object from the database table by field name.
        :param name: name value
        :return: Master object
        """
        return self._session.query(Master).filter(Master.name == name).first()

    def find_by_surname(self, surname: str) -> Master:
        """
        Gets Master object from the database table by field surname.
        :param surname: surname value
        :return: Master object
        """
        return self._session.query(Master).filter(Master.surname == surname).first()

    def find_by_name_and_surname(self, name: str, surname: str) -> Master:
        """
        Gets Master object from the database table by fields name and surname.
        :param name: name value
        :param surname: surname value
        :return: Master object
        """
        return (
            self._session.query(Master)
            .filter(Master.name == name, Master.surname == surname)
            .first()
        )

    def find_by_phone_number(self, phone_number: int) -> Master:
        """
        Gets Master object from the database table by field phone_number.
        :param phone_number: phone_number value
        :return: Master object
        """
        return self._session.query(Master).filter(Master.phone_number == phone_number).first()

    def find_by_id(self, master_id: int) -> Master:
        """
        Gets Master object from the database table by ID.
        :param master_id: ID of the film
        :return: Master object
        """
        return self._session.query(Master).get(master_id)

    def find_all(self):
        return Master.query.all()
