"""
2023
Nataliia.Parkhomchuk.IR.2022@lpnu.ua
© Nataliia Parkhomchuk
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Company(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "company"

    company_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    company_name = db.Column(db.String(45), nullable=False)
    company_addres = db.Column(db.String(45), nullable=False)
    contact_person = db.Column(db.String(45), nullable=False)
    contact_email = db.Column(db.String(45), nullable=False)

    def __repr__(self) -> str:
        return f"Company({self.company_id}, '{self.company_name}', '{self.company_addres}', '{self.contact_person}', '{self.contact_email}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.company_id,
            "company name": self.company_name,
            "company address": self.company_addres,
            "contact person": self.contact_person,
            "contact email": self.contact_email
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> 'Company':
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Company(
            company_name=dto_dict.get("company name"),
            company_address=dto_dict.get("company address"),
            contact_person=dto_dict.get("contact person"),
            contact_email=dto_dict.get("contact email"),
        )
        return obj