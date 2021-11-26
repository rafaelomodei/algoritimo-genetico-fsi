from copy import copy
from typing import List
from discipline import Discipline
from readFile import readFile
from createChromosomes import createChromosomes
from utils.constants import INITIAL_POPULATION

def createFistPopulation(chromosomesList: List[Discipline]):
    listPopulation: List[List[Discipline]] = list()

    for population in range(INITIAL_POPULATION):
        
        print('População: ', population) 

        chromosomes: List[Discipline] = createChromosomes(chromosomesList.copy())
        listPopulation.append(chromosomes)

        for discipline in chromosomes:
            print(
                'ID: ', discipline.id,
                'Nome: ', discipline.name,
                'Professor: ', discipline.teacher,
                'Horas semanais: : ', discipline.weeklyWorkload,
                'Posições: ', discipline.positions,
                'Dependencia: ', discipline.dependencies,
                'Periodo: ', discipline.timeCourse,
                'Penalidade: ', discipline.penalty,
            )
    
    return listPopulation