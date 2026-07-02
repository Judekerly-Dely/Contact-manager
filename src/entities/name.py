from datetime import datetime, timezone

def _now() -> datetime:
    return datetime.now(timezone.utc)


class Name:

    def __init__(self, content: str):

        self.updated_at = _now()

        if not self.validate(content):
            raise ValueError(f"{content} is invalid.")
        
        self.content = content      
        
    def validate(content: str) -> bool:
        """For Validating the name"""
        return content.isalpha()
    
    def __str__(self):
        return self.content
    
    def change(self, new_content: str) -> None:
        if not self.validate(new_content):
            raise ValueError(f"{new_content} is invalid.")
        self.content = new_content
        self.updated_at = _now()

class Firstname(Name):
    pass


class Lastname(Name):
    pass