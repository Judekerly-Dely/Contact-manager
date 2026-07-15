#this file represents the condition for a phone number (haitian), to be accepted by the system

class Number:
    def __init__(self, number: str):

        if not self.validate(number):
            return False
        self.number = number

    def validate(content: str) -> bool:
        """For Validating the phone number"""

        if not content.startswith("+509") and len(content) == 8:
            content = str(f'+509{content}')
        return content.isalpha()    

    def __str__(self):
        return self.number
        

