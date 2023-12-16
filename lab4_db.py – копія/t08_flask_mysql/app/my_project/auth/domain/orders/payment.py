"""
2023
Nataliia.Parkhomchuk.IR.2022@lpnu.ua
© Nataliia Parkhomchuk
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Payment(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "payment"

    payment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    record_id = db.Column(db.Integer, db.ForeignKey('service_records.record_id'), nullable=False)
    payment_date = db.Column(db.Date, nullable=False)
    payment_amoun = db.Column(db.Integer, nullable=False)



    def __repr__(self) -> str:
        return f"Terminal({self.payment_id}, '{self.record_id}', '{self.payment_date}', '{self.payment_amoun}'')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "payment_id": self.payment_id,
            "record_id": self.record_id,
            "payment_date": self.payment_date,
            "payment_amoun": self.payment_amoun
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> 'Payment':
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Payment(
            record_id=dto_dict.get("record_id"),
            payment_date=dto_dict.get("payment_date"),
            payment_amoun=dto_dict.get("payment_amoun")
        )
        return obj
