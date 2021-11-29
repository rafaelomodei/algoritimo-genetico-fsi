from typing import List
from model.chromosome import Chromosome

class Population:

    id: int = 0
    populationsList: List[Chromosome]
    penalty: float

    def __init__(self, penalty: int):
        self.penalty = penalty
