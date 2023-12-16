"""
2023
Nataliia.Parkhomchuk.IR.2022@lpnu.ua
© Nataliia Parkhomchuk
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Master(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "masters"

    master_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    master_name = db.Column(db.String(45), nullable=False)
    master_surname = db.Column(db.String(45), nullable=False)
    master_phone = db.Column(db.Integer, nullable=False)

    def __repr__(self) -> str:
        return f"Master({self.master_id}, '{self.master_name}', '{self.master_surname}', '{self.master_phone}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "master_id": self.master_id,
            "master_name": self.master_name,
            "master_surname": self.master_surname,
            "master_phone": self.master_phone
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> 'Master':
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Master(
            master_name=dto_dict.get("master_name"),
            master_surname=dto_dict.get("master_surname"),
            master_phone=dto_dict.get("master_phone")
        )
        return obj
