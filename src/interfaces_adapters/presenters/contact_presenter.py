from src.entities.contact import Contact
from typing import Any, Dict, List


class ContactPresenter:


    @staticmethod
    def to_dict(contact: Contact) -> Dict[str, Any]:


        return{
            "id": contact.contact_id,
            "firstname": contact.first_name,
            "lastname": contact.last_name,
            "email": contact.email,
            "number": contact.phone,
            "birthday": contact.birthday,
            "status": contact.status,
            "created_at": contact.created_at.isoformat()
        }
    
    @staticmethod
    def to_list(contact: List[Contact]) -> List[Dict[str, Any]]:
        return [ContactPresenter.dict(c) for c in contact]
    

    @staticmethod
    def cli_presentation(contact: Contact) -> str:
        lines = [
            f"  ID          : {contact.contact_id}",
            f"  Telephone   : {contact.phone}",
            f"  Firstname   : {contact.first_name}",
            f"  Lastname    : {contact.last_name}",
            f"  Birthday    : {contact.birthday or '(none)'}",
            f"  Status      : {contact.status.value}",
            f"  Created     : {contact.created_at.strftime('%Y-%m-%d %H:%M')}",
            f"  Updated     : {contact.updated_at.strftime('%Y-%m-%d %H:%M')}",
        ]
        return "\n".join(lines)
