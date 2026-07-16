from typing import Any, Dict, Optional
from src.interfaces_adapters.presenters.contact_presenter import ContactPresenter
from src.use_cases.create import CreateContactUseCase, CreateContactInput
from src.use_cases.delete import DeleteContactUseCase, DeleteContactInput
from src.use_cases.filter_contact import FilterContactUseCase, FilterContactInput
from src.use_cases.interfaces.contact_repository import ContactRepository

class ContactController:

    def __init__(self, repository: ContactRepository):

        self.create_usecase = CreateContactUseCase(repository)
        self.delete_usecase = DeleteContactUseCase(repository)
        self.filter_usecase = FilterContactUseCase(repository)

    def create_contact(self, data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            output = self.create_usecase.execute(
                CreateContactInput(
                    first_name=data["first_name"],
                    last_name=data["last_name"],
                    phone=data["phone"]))

            return {
                "success": True,
                "contact": ContactPresenter.to_dict(output.contact)}

        except ValueError as e:
            return {
                "success": False,
                "message": str(e)}

    def delete_contact(self, contact_id: int):

        output = self.delete_usecase.execute(
            DeleteContactInput(contact_id))

        return {
            "success": output.success}

    def filter_contact(self,data: Optional[Dict[str, Any]] = None):

        if data is None:
            input_data = FilterContactInput()

        else:
            input_data = FilterContactInput(
                contact_id=data.get("contact_id"),
                first_name=data.get("firstname"),
                last_name=data.get("lastname"),
                phone=data.get("phone"),
                tag=data.get("tag"),
                status=data.get("status"))

        output = self.filter_usecase.execute(input_data)

        return {
            "success": True,
            "contacts": ContactPresenter.to_list(output.contacts),
            "total": output.total}
    
   