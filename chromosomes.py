from typing import List
from discipline import Discipline
from punishments import Punishments


class Chromosomes:

    id: int
    fitness: float
    disciplineList: List[Discipline]
    punishmentsList: List[Punishments]

    def __init__(self,  id: int, disciplineList: List[Discipline]):
        self.id = id,
        self.disciplineList = disciplineList