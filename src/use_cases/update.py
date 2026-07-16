from dataclasses import dataclass
from typing import Optional

from src.entities.contact import Contact
from src.use_cases.interfaces.contact_repository import ContactRepository


@dataclass
class UpdateContactInput:
    contact_id: int
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    number: Optional[str] = None
    email: Optional[str] = None
    birthday: Optional[str] = None
    tag: Optional[str] = None


@dataclass
class UpdateContactOutput:
    contact: Contact


class UpdateContactUseCase:

    def __init__(self, repository: ContactRepository):
        self.repository = repository

    def execute(self, input_data: UpdateContactInput) -> UpdateContactOutput:

        contact = self.repository.get_by_id(input_data.contact_id)

        if contact is None:
            raise ValueError("Contact not found.")

        if input_data.firstname is not None:
            contact.first_name = input_data.firstname

        if input_data.lastname is not None:
            contact.last_name = input_data.lastname

        if input_data.number is not None:
            contact.phone = input_data.number

        if input_data.email is not None:
            contact.email = input_data.email

        if input_data.birthday is not None:
            contact.birthday = input_data.birthday

        if input_data.tag is not None:
            contact.tag = input_data.tag

        self.repository.update(contact)

        return UpdateContactOutput(contact)