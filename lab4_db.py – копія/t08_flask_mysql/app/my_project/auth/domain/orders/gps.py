"""
2023
Nataliia.Parkhomchuk.IR.2022@lpnu.ua
© Nataliia Parkhomchuk
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Gps(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "gps"

    gps_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    gps_latitude = db.Column(db.Integer, nullable=False)
    gps_longitude = db.Column(db.Integer, nullable=False)
    

    def __repr__(self) -> str:
        return f"Gps({self.gps_id}, '{self.gps_latitude}', '{self.gps_longitude}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "gps_id": self.gps_id,
            "gps_latitude": self.gps_latitude,
            "gps_longitude": self.gps_longitude
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> 'Gps':
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Gps(
            gps_latitude=dto_dict.get("gps_latitude"),
            gps_longitude=dto_dict.get("gps_longitude"),
        )
        return obj
