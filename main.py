import copy
from typing import List
from discipline import Discipline
from readFile import readFile
from createFirstGeneration import createFirstGeneration

INITIAL_POPULATION = 5


disciplineList: list = readFile('disciplinas_1_4_utfpr_sh.json')


for population in range(0, INITIAL_POPULATION):
    listPopulation: list = list()

    individuo: List[Discipline] = copy.deepcopy(createFirstGeneration(disciplineList))
    listPopulation.append(listPopulation)

    print('>>>>>> POPPULATION ', population)

    for discipline in individuo:
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
