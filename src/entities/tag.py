class Tag:
    def __init__(self, tag: str):
        self.tag = tag

    def __str__(self):
        return self.tag
    
    def change(self, new_tag: str) -> None:
        self.tag = new_tag

    def delete(self) -> None:
        self.tag = None
    
    def add_tag(self):
        if self.tag is None:
            self.tag = ""