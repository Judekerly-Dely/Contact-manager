#this file represents the conditions for an email to be accepted by the system
class Email:
    """A class representing an email address and the validation condition."""

    def __init__(self, address: str):

        if not self.validate(address):
            return False
        self.address = address

    def __str__(self):
        return self.address
    
    def validate(content: str) -> bool:
        """For Validating the email address"""
        if not content:
            return False
        return "@" in content and "." in content