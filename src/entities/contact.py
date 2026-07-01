from datetime import datetime, timezone
from dataclasses import field, dataclass
from enum import Enum
from src.entities.email import Email
from src.entities.name import Firstname, Lastname
from src.entities.number import Number

def _now() -> datetime:
    return datetime.now(timezone.utc)

class ContactStatus(Enum):
    """The different status of a contact in the system"""

    ACTIVE = "active"
    SUSPENDED = "suspended"
    DELETED = "deleted"
    BLOCKED = "blocked"


@dataclass
class Contact:    

    contact_id: str  
    first_name: Firstname
    last_name: Lastname
    email: Email
    phone: Number
    status: ContactStatus = field(default_factory = ContactStatus.ACTIVE)
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


    def change_status(self, new_status: ContactStatus) -> None:
        self.status = new_status
        self.updated_at = _now()

    def is_blocked(self):
        self.updated_at = _now()
        return self.status == ContactStatus.BLOCKED

    def is_suspended(self):
        self.updated_at = _now()
        return self.status == ContactStatus.SUSPENDED

    def is_deleted(self):
        self.updated_at = _now()
        return self.status == ContactStatus.DELETED

    def is_active(self):
        self.updated_at = _now()
        return self.status == ContactStatus.ACTIVE


    

