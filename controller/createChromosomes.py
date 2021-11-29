import random
from model.chromosome import Chromosome
from model.utils.constants import MAX_NUMBER_TIME_CORSE

def createChromosomes(chromosome: Chromosome) -> Chromosome:

    chromosome.id = chromosome.id + 1
    for timeCourse in range(1, MAX_NUMBER_TIME_CORSE):
        #range é a a quantidade de disciplinas que cabem na semana
        disciplinePosition = random.sample(range(0, 25), 25)
        for disciplene in chromosome.disciplineList:
            if disciplene.timeCourse == timeCourse: 
                disciplene.positions = [] # Zera os horarios, para garantir que não vai ter nenhum horario
                for x in range(0, disciplene.weeklyWorkload):
                    disciplene.positions.append(disciplinePosition.pop())
                
    return chromosome

