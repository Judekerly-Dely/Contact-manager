from abc import ABC, abstractmethod
from src.entities.contact import Contact, ContactStatus
from typing import Optional, List


class ContactRepository(ABC):

    @abstractmethod
    def create(self, contact: Contact) -> Contact:
        ...

    @abstractmethod
    def delete(self, contact_id: int) -> bool:
        ...

    @abstractmethod
    def get_by_id(self, contact_id: int) -> Optional[Contact]:
        ...

    @abstractmethod
    def get_by_firstname(self, firstname: str) -> List[Contact]:
        ...

    @abstractmethod
    def get_by_lastname(self, lastname: str) -> List[Contact]:
        ...

    @abstractmethod
    def get_by_status(self, status) -> List[Contact]:
        ...

    @abstractmethod
    def get_by_tag(self, tag : str) -> List[Contact]:
        ...

    @abstractmethod
    def get_by_number(self, number : str) -> Optional[Contact]:
        ...

    @abstractmethod
    def get_all(self) -> List[Contact]:
        ...

    @abstractmethod
    def update(self, contact: Contact) -> Contact:
        ...





