from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class ServiceMasterAvailability(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "service_master_availability"

    availability_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    master_id = db.Column(db.Integer, db.ForeignKey('masters.master_id'), nullable=False)
    available_date = db.Column(db.Date, nullable=False)


    def __repr__(self) -> str:
        return f"ServiceMasterAvailability({self.availability_id}, '{self.master_id}', '{self.available_date}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "availability_id": self.availability_id,
            "master_id": self.master_id,
            "available_date": self.available_date
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> 'ServiceMasterAvailability':
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = ServiceMasterAvailability(
            master_id=dto_dict.get("master_id"),
            available_date=dto_dict.get("available_date")
        )
        return obj
