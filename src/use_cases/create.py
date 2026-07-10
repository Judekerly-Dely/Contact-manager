from dataclasses import dataclass
from entities.contact import Contact
from interfaces import ContactRepository

@dataclass
class CreateContactInput:
    firstname: str
    lastname: str
    email: str
    phone: str

@dataclass
class CreateContactOutput:
    contact: Contact

class CreateContactUseCase:
    def __init__(self, contact_repository: ContactRepository):
        self.contact_repository = contact_repository

    def execute(self, input_data: CreateContactInput) -> CreateContactOutput:
        contact = Contact(
            firstname=input_data.firstname,
            lastname=input_data.lastname,
            email=input_data.email,
            phone=input_data.phone,
            tag = None
        )
        
        created_contact = self.contact_repository.create(contact)
        return CreateContactOutput(contact=created_contact)