"""
2023
Nataliia.Parkhomchuk.IR.2022@lpnu.ua
© Nataliia Parkhomchuk
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Service(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "services"

    service_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    service_type = db.Column(db.String(45), nullable=False)

    terminals = db.relationship("Terminal_Service", back_populates="service")

    def __repr__(self) -> str:
        return f"Service({self.service_id}, '{self.service_type}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "service_id": self.service_id,
            "service_type": self.service_type
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> 'Service':
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Service(
            service_type=dto_dict.get("service_type")
        )
        return obj
