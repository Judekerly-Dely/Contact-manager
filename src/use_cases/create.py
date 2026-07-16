from dataclasses import dataclass
from src.entities.contact import Contact
from src.use_cases.interfaces.contact_repository import ContactRepository

@dataclass
class CreateContactInput:
    first_name: str
    last_name: str
    phone: str

@dataclass
class CreateContactOutput:
    contact: Contact

class CreateContactUseCase:
    def __init__(self, contact_repository: ContactRepository):
        self.contact_repository = contact_repository

    def execute(self, input_data: CreateContactInput) -> CreateContactOutput:
        contact = Contact(
            contact_id= input_data.contact_id,
            first_name=input_data.first_name,
            last_name=input_data.last_name,
            phone=input_data.phone,
        )
        
        created_contact = self.contact_repository.create(contact)
        return CreateContactOutput(contact=created_contact)