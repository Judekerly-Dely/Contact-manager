#this file is the entity for the contact manager system. It guarantees that no rule or broken and the system can run smoothly
from enum import Enum
from src.entities.email import Email
from src.entities.name import Firstname, Lastname
from src.entities.number import Number
from src.entities.tag import Tag
from src.entities.birthday import Birthday
from datetime import datetime, timezone
from dataclasses import dataclass, field
from typing import Optional

def _now() -> datetime:
    return datetime.now(timezone.utc)

class ContactStatus(Enum):
    """The different status of a contact in the system"""

    ACTIVE = "active"
    SUSPENDED = "suspended"
    DELETED = "deleted"
    BLOCKED = "blocked"
    FAVORITE = "favorite"

class ContactFamiliarity(Enum):
    """The different familiarity of a contact in the system"""

    OTHER = "other"
    FAVORITE = "favorite"
    PROFESSIONAL = "professional"


@dataclass
class Contact:    

    contact_id: int
    first_name: Firstname
    last_name: Lastname
    phone: Number
    email: Optional[Email] = None
    tag: Optional[Tag] = None
    birthday: Optional[Birthday] = None
    status: ContactStatus = field(default_factory = lambda: ContactStatus.ACTIVE)
    statusfamiliarity: ContactFamiliarity = field(default_factory = lambda: ContactFamiliarity.OTHER)
    created_at: datetime = field(default_factory=_now)
    updated_at: datetime = field(default_factory=_now)

    def _post_init_(self):
        if self.contact_id <= 0:
            return False
        self.contact_id = self.contact_id

    def change_status(self, new_status: ContactStatus) -> None:
        self.status = new_status
        self.updated_at = _now()

    def is_favorite(self):
        self.updated_at = _now()
        return self.statusfamiliarity == ContactFamiliarity.FAVORITE
    
    def set_other(self):
        self.updated_at = _now()
        if self.statusfamiliarity != ContactFamiliarity.OTHER:
            self.statusfamiliarity = ContactFamiliarity.OTHER

    def set_favorite(self):
        self.statusfamiliarity = ContactFamiliarity.FAVORITE

    def set_professional(self):
        self.statusfamiliarity = ContactFamiliarity.PROFESSIONAL

    def is_professional(self):
        return self.statusfamiliarity == ContactFamiliarity.PROFESSIONAL

    def is_blocked(self):
        return self.status == ContactStatus.BLOCKED

    def is_suspended(self):
        return self.status == ContactStatus.SUSPENDED

    def is_deleted(self):
        return self.status == ContactStatus.DELETED

    def is_active(self):
        return self.status == ContactStatus.ACTIVE


    

