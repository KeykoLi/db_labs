"""
2023
Nataliia.Parkhomchuk.IR.2022@lpnu.ua
© Nataliia Parkhomchuk
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class ServiceRecord(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "service_records"

    record_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    terminal_id = db.Column(db.Integer, db.ForeignKey('terminals.terminal_id'), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('services.service_id'), nullable=False)
    master_id = db.Column(db.Integer, db.ForeignKey('masters.master_id'), nullable=False)
    service_date = db.Column(db.Date, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Integer, nullable=False)

    services = db.relationship('Service', backref='service_records')

    def __repr__(self) -> str:
        return (f"Master({self.record_id}, '{self.terminal_id}', '{self.service_id}', '{self.master_id}'"
                f", '{self.service_date}', '{self.duration}', '{self.total_price}')")

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "record_id": self.record_id,
            "terminal_id": self.terminal_id,
            "service_id": self.service_id,
            "master_id": self.master_id,
            "service_date": self.service_date,
            "duration": self.duration,
            "total_price": self.total_price
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> 'ServiceRecord':
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = ServiceRecord(
            terminal_id=dto_dict.get("terminal_id"),
            service_id=dto_dict.get("service_id"),
            master_id=dto_dict.get("master_id"),
            service_date=dto_dict.get("service_date"),
            duration=dto_dict.get("duration"),
            total_price=dto_dict.get("total_price")
        )
        return obj
