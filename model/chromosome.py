from typing import List
from model.discipline import Discipline


class Chromosome:

    id: int
    disciplineList: List[Discipline]
    penalty: float = 0

    def __init__(self, disciplineList: List[Discipline]):
        self.disciplineList = disciplineList