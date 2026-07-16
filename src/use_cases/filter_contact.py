from src.entities.contact import Contact, ContactStatus
from src.use_cases.interfaces.contact_repository import ContactRepository
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass
class FilterContactInput:
    contact_id: Optional[int] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    status: Optional[ContactStatus] = None
    phone: Optional[str] = None
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
            contacts = [c for c in contacts if c.contact_id == input_data.contact_id]

        if input_data.first_name:
            contacts = [c for c in contacts if c.first_name.lower() == input_data.first_name.lower()]

        if input_data.last_name:
            contacts = [c for c in contacts if c.last_name.lower() == input_data.last_name.lower()]

        if input_data.status:
            contacts = [c for c in contacts if c.status == input_data.status]

        if input_data.phone:
            contacts = [c for c in contacts if input_data.phone in c.phone]

        if input_data.tag:
            contacts = [
                c for c in contacts
                if input_data.tag in c.tags
            ]
        contacts = sorted(contacts, key=lambda c: c.created_at, reverse=True)
        return FilterContactOutput(contacts=contacts)
    
class get_all:
    def __init__(self, repository: ContactRepository) -> None:
        self.repository = repository

    def execute(self) -> FilterContactOutput:
        contacts = self.repository.get_all()
        contact_sorted = sorted(contacts, key=lambda c: c.created_at, reverse=True)
        return FilterContactOutput(contacts=contact_sorted)