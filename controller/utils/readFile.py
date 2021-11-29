import json
from typing import List
from io import TextIOWrapper
from model.chromosome import Chromosome
from model.discipline import Discipline

def readFile(file: str) -> Chromosome:
    disciplineList: List[Discipline] = list()

    with open(file, 'r', encoding='utf8') as ctx:
        data: TextIOWrapper = json.load(ctx)

        for discipline in data:
            currentDiscipline: Discipline = Discipline(
                discipline['id'],
                discipline['name'],
                discipline['teacher'],
                discipline['weeklyWorkload'],
                discipline['dependencies'],
                discipline['timeCourse'],
            )
            disciplineList.append(currentDiscipline)
    chromosome: Chromosome = Chromosome(disciplineList)
    chromosome.id = 0
    
    return chromosome
