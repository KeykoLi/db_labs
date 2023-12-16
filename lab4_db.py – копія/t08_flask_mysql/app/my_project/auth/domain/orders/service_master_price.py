from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class ServiceMasterPrice(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "service_master_prices"

    price_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    service_id = db.Column(db.Integer, db.ForeignKey('services.service_id'), nullable=False)
    master_id = db.Column(db.Integer, db.ForeignKey('masters.terminal_id'), nullable=False)
    price = db.Column(db.Integer, nullable=False)

    def __repr__(self) -> str:
        return f"Service({self.price_id}, '{self.service_type}', '{self.master_id}', '{self.price}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "price_id": self.price_id,
            "service_id": self.service_id,
            "master_id": self.master_id,
            "price": self.price
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> 'ServiceMasterPrice':
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = ServiceMasterPrice(
            service_id=dto_dict.get("service_id"),
            master_id = dto_dict.get("master_id"),
            price=dto_dict.get("price")
        )
        return obj
