from dataclasses import dataclass
from interfaces import ContactRepository

@dataclass
class DeleteContactInput:
    contact_id: int

@dataclass
class DeleteContactOutput:
    success: bool

class DeleteContactUseCase:
    def __init__(self, contact_repository: ContactRepository):
        self.contact_repository = contact_repository

    def execute(self, input_data: DeleteContactInput) -> DeleteContactOutput:
        success = self.contact_repository.delete(input_data.contact_id)
        return DeleteContactOutput(success=success)