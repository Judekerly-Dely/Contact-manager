#this file represents the condition for a firstname or lastname to be accepted by the system

from datetime import datetime, timezone

def _now() -> datetime:
    return datetime.now(timezone.utc)


class Name:

    def __init__(self, content: str):

        if not self.validate(content):
            return False
        
        self.updated_at = _now()
        self.content = content                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
        
    def validate(content: str) -> bool:
        """For Validating the name"""
        return content.isalpha()
    
    def __str__(self):
        return self.content
    
    def change(self, new_content: str) -> None:
        if not self.validate(new_content):
            return False
        self.content = new_content
        self.updated_at = _now()
        return True

class Firstname(Name):
    ...


class Lastname(Name):
    ...