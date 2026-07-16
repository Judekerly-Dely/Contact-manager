from typing import Dict, List, Optional
import copy

from src.entities.contact import Contact
from src.use_cases.interfaces.contact_repository import ContactRepository


class InMemoryContactRepository(ContactRepository):
    def __init__(self):
        self._contacts: Dict[int, Contact] = {}
        self._next_id = 1

    def create(self, contact: Contact) -> Contact:
        contact.id = self._next_id

        self._contacts[contact.id] = copy.deepcopy(contact)

        self._next_id += 1

        return copy.deepcopy(contact)

    def delete(self, contact_id: int) -> bool:
        if contact_id not in self._contacts:
            return False
        del self._contacts[contact_id]
        return True


    def get_by_id(self, contact_id: int) -> Optional[Contact]:
        contact = self._contacts.get(contact_id)

        if not contact:
            return None

        return copy.deepcopy(contact)

    def get_by_firstname(self, firstname: str) -> List[Contact]:
        return [
            copy.deepcopy(contact)
            for contact in self._contacts.values()
            if contact.firstname.lower() == firstname.lower()
        ]
    
    def get_by_lastname(self, lastname: str) -> List[Contact]:
        return [
            copy.deepcopy(contact)
            for contact in self._contacts.values()
            if contact.lastname.lower() == lastname.lower()
        ]
    
    def get_by_status(self, status) -> List[Contact]:
        return [
            copy.deepcopy(contact)
            for contact in self._contacts.values()
            if contact.status == status
        ]
    
    def get_by_tag(self, tag: str) -> List[Contact]:
        return [
            copy.deepcopy(contact)
            for contact in self._contacts.values()
            if tag in contact.tags
        ]
    
    def get_all(self) -> List[Contact]:
        return [
            copy.deepcopy(contact)
            for contact in self._contacts.values()
        ]
    
    def get_by_number(self, number: str) -> Optional[Contact]:
        for contact in self._contacts.values():
            if contact.phone_number == number:
                return copy.deepcopy(contact)
        return None
    
    def update(self, contact: Contact) -> Contact:

        if contact.id not in self._contacts:
            raise ValueError("Contact not found")

        self._contacts[contact.id] = copy.deepcopy(contact)

        return copy.deepcopy(contact)
    
