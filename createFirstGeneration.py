import random
from typing import List
from discipline import Discipline

MAX_NUMBER_TIME_CORSE = 4

def createFirstGeneration(disciplineList: List[Discipline]):

    for timeCourse in range(1, MAX_NUMBER_TIME_CORSE):
        #range é a a quantidade de disciplinas que cabem na semana
        disciplinePosition = random.sample(range(0, 25), 25)
        for disciplene in disciplineList:
            if disciplene.timeCourse == timeCourse:
                disciplene.positions = [] # Zera os horarios, para garantir que não vai ter nenhum horario
                for x in range(0, disciplene.weeklyWorkload):
                    disciplene.positions.append(disciplinePosition.pop())
                
    return disciplineList

