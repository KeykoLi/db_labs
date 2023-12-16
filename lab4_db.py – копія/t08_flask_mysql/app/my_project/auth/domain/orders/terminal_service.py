"""
2023
Nataliia.Parkhomchuk.IR.2022@lpnu.ua
© Nataliia Parkhomchuk
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Terminal_Service(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "terminal_services"

    terminal_id = db.Column(db.Integer, db.ForeignKey('terminals.terminal_id'), primary_key=True)
    service_id = db.Column(db.Integer, db.ForeignKey('services.service_id'), primary_key=True)

    terminal = db.relationship("Terminal", back_populates="services")
    service = db.relationship("Service", back_populates="terminals")

    def __repr__(self) -> str:
        return f"Terminal({self.terminal_id}, '{self.service_id}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "terminal_id": self.terminal_id,
            "service_id": self.service_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> 'Terminal_Service':
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Terminal_Service(
            address=dto_dict.get("address"),
            service_id=dto_dict.get("service_id"),
        )
        return obj
