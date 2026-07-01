class Number:
    def __init__(self, number: str):

        if not self.validate(number):
            raise ValueError(f"{number} is an invalid phone number.")
        self.number = number

    def validate(content: str) -> bool:
        """For Validating the phone number"""

        if not content.startswith("+509"):
            content = str(f'+509{content}')
        return content.isalpha()    

    def __str__(self):
        return self.number
        

