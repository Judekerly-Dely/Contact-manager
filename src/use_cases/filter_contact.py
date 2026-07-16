from src.entities.contact import Contact, ContactStatus
from src.use_cases.interfaces.contact_repository import ContactRepository
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass
class FilterContactInput:
    contact_id: Optional[int] = None
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    status: Optional[ContactStatus] = None
    number: Optional[str] = None
    tag: Optional[str] = None

@dataclass
class FilterContactOutput:
    contacts: List[Contact] = field(default_factory=list)
    total: int = 0

    def __post_init__(self):
        self.total = len(self.contacts)

class FilterContactUseCase:

    def __init__(self, repository: ContactRepository) -> None:
        self.repository = repository

    def execute(self, input_data: FilterContactInput) -> FilterContactOutput:

        contacts = self.repository.get_all()

        if input_data.contact_id is not None:
            contacts = [c for c in contacts if c.id == input_data.contact_id]

        if input_data.firstname:
            contacts = [c for c in contacts if c.firstname.lower() == input_data.firstname.lower()]

        if input_data.lastname:
            contacts = [c for c in contacts if c.lastname.lower() == input_data.lastname.lower()]

        if input_data.status:
            contacts = [c for c in contacts if c.status == input_data.status]

        if input_data.number:
            contacts = [c for c in contacts if input_data.number in c.numbers]

        if input_data.tag:
            contacts = [
                c for c in contacts
                if input_data.tag in c.tags
            ]
        contacts = sorted(contacts, key=lambda c: c.created_at, reverse=True)
        return FilterContactOutput(contacts=contacts)