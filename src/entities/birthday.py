from dataclasses import dataclass


@dataclass
class Infos:
    day: int
    month: int
    year: int

class Birthday:
    def __init__(self, infos: Infos):
        self.day = infos.day
        self.month = infos.month
        self.year = infos.year

    def __str__(self):
        return f"{self.day:02d}/{self.month:02d}/{self.year}"