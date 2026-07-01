
class Email:
    """A class representing an email address."""

    def __init__(self, address: str):

        if not self.validate(address):
            raise ValueError(f"{address} is an invalid email address.")
        self.address = address

    def __str__(self):
        return self.address
    
    def validate(content: str) -> bool:
        """For Validating the email address"""
        if not content:
            raise ValueError("Email address cannot be empty.")
        return "@" in content and "." in content