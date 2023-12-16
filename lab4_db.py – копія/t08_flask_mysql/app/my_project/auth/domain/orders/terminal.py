"""
2023
Nataliia.Parkhomchuk.IR.2022@lpnu.ua
© Nataliia Parkhomchuk
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Terminal(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "terminals"

    terminal_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    address = db.Column(db.String, nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey('company.company_id'), nullable=False)
    gps_id = db.Column(db.Integer, db.ForeignKey('gps.gps_id'), nullable=False)
    installation_date = db.Column(db.Date, nullable=False)

    services = db.relationship("Terminal_Service", back_populates="terminal")

    def __repr__(self) -> str:
        return f"Terminal({self.terminal_id}, '{self.address}', '{self.company_id}', '{self.gps_id}', '{self.installation_date}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "terminal_id": self.terminal_id,
            "address": self.address,
            "company_id": self.company_id,
            "gps_id": self.gps_id,
            "installation_date": self.installation_date
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> 'Terminal':
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Terminal(
            address=dto_dict.get("address"),
            company_id=dto_dict.get("company_id"),
            gps_id=dto_dict.get("gps_id"),
            installation_date=dto_dict.get("installation_date")
        )
        return obj
