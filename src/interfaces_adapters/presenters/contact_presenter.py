from typing import Any, Dict, List
from src.entities.contact import Contact
class ContactPresenter:

    @staticmethod
    def to_dict(contact: Contact) -> Dict[str, Any]:

        return {

            "contact_id": contact.contact_id,
            "firstname": str(contact.first_name),
            "lastname": str(contact.last_name),
            "phone": str(contact.phone),
            "email": str(contact.email) if contact.email else None,
            "tag": str(contact.tag) if contact.tag else None,
            "birthday": (contact.birthday.isoformat() if contact.birthday else None),
            "status": contact.status.value,
            "created_at": contact.created_at.isoformat(),
            "updated_at": contact.updated_at.isoformat()}

    @staticmethod
    def to_list(contacts: List[Contact]) -> List[Dict[str, Any]]:
        return [
            ContactPresenter.to_dict(c)
            for c in contacts]
    
    @staticmethod
    def cli_presentation(contact: Contact) -> str:
        lines = [
            f"  ID          : {contact.contact_id}",
            f"  Telephone   : {contact.phone}",
            f"  Firstname   : {contact.first_name}",
            f"  Lastname    : {contact.last_name}",
            f"  Birthday    : {contact.birthday.isoformat() if contact.birthday else None}",
            f"  Status      : {contact.status.value}",
            f"  Created     : {contact.created_at.strftime('%Y-%m-%d %H:%M')}",
            f"  Updated     : {contact.updated_at.strftime('%Y-%m-%d %H:%M')}",
        ]
        return "\n".join(lines)