from typing import Dict, Any, Optional
from src.entities.contact import Contact
from src.use_cases.create import CreateContactUseCase, CreateContactInput
from src.use_cases.delete import DeleteContactUseCase,DeleteContactInput
from src.use_cases.filter_contact import FilterContactUseCase,FilterContactInput
from src.use_cases.interfaces.contact_repository import ContactRepository
from src.interfaces_adapters.presenters.contact_presenter import ContactPresenter


class ContactController:

    def __init__(self, repository: ContactRepository):

        self.create_usecase = CreateContactUseCase(repository)
        self.delete_usecase = DeleteContactUseCase(repository)
        self.filter_usecase = FilterContactUseCase(repository)


    def create_contact(self, data: Dict[str, Any]) -> Dict[str, Any]:

        first_name = data.get("first_name", "").strip()
        last_name = data.get("last_name", "").strip()
        phone = data.get("phone", "").strip()

        if not first_name or not last_name or not phone:
            return {
                "success": False,
                "message": "Missing required informations"
            }

        try:
            contact_input = CreateContactInput(
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                email=data.get("email"),
                tags=data.get("tags", [])
            )
            output = self.create_usecase.execute(contact_input)
            return {
                "success": True,
                "contact": ContactPresenter.present(output.contact)
            }
        
        except ValueError as e:

            return {
                "success": False,
                "message": str(e)
            }

    def delete_contact(self, contact_id: int) -> Dict[str,Any]:

        output = self.delete_usecase.execute(DeleteContactInput(contact_id=contact_id))
        return {
            "success": output.deleted,
            "message": output.message
        }

    def filter_contact(self, data: Optional[Dict[str,Any]]=None) -> Dict[str,Any]:

        try:
            contact = None
            if data:
                contact = Contact(
                    id=data.get("id"),
                    first_name=data.get("first_name"),
                    last_name=data.get("last_name"),
                    phone=data.get("phone"),
                    email=data.get("email"),
                    status=data.get("status"),
                    tags=data.get("tags", [])
                )

            output = self.filter_usecase.execute(
                FilterContactInput(contact_info=contact))
            
            return {
                "success": True,
                "contacts": ContactPresenter.filter(output.contacts),
                "total": len(output.contacts)
            }

        except ValueError as e:

            return {
                "success": False,
                "message": str(e)
            }