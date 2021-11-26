
from typing import List
from punishments import Punishments
from discipline import Discipline
from utils.constants import INITIAL_POPULATION, MAX_NUMBER_TIME_CORSE


# verificar se a disciplina do mesmo periodo está ocupando o mesmo horario de outra disciplina
def classesOverlap(discipleneList: List[Discipline]):
    """Verifica se a disciplina atual tem conflito de horario com outra disciplina"""

    totalPunishments: int = 0
    positionsOccupied: list[int] = list()

    for discipline in discipleneList:
        for timeCourse in range(MAX_NUMBER_TIME_CORSE):
            positionsOccupied.clear()
            if discipline.timeCourse == timeCourse:
                for disciplinePositions in discipline.positions:

                    print('------')
                    print('Periodo', discipline.timeCourse)
                    print('Verificando posição: ', disciplinePositions)
                    print('Disciplina Lista: ', discipline.id)
                    print('Disciplina Lista periodo: ', discipline.timeCourse)
                    print('Disciplina Lista posições: ', discipline.positions)
                    print('Posições ocupadas: ', positionsOccupied)
                    print('Punições: ', totalPunishments)
                    print('------')

                    if disciplinePositions in positionsOccupied:
                        totalPunishments = totalPunishments + Punishments.classesOverlap
                    else:
                        positionsOccupied.append(disciplinePositions)
    
    return totalPunishments

def disorderedDependencies(discipleneList: List[Discipline]):
    """Verifica se as dependências estão desordenadas... exem: calculo 2 vim antes de calculo 1"""

    totalPunishments: int = 0
    disciplineVisitedList: List[Discipline] = list()

    for discipline in discipleneList:
        for dependencieID in discipline.dependencies:
            for disciplineVisited in disciplineVisitedList:
                if dependencieID == disciplineVisited.id and  disciplineVisited.timeCourse > discipline.timeCourse:
                    totalPunishments = totalPunishments + Punishments.disorderedDependencies    

                print('------')
                print('Disciplina Lista: ', discipline.id)
                print('Disciplina Lista PERIODO: ', discipline.timeCourse)
                print('Disciplina Lista DEPENDENCIA: ', discipline.dependencies)
                print('')
                print('dependencieID: ', dependencieID)
                print('')
                print('Disciplina Visitada: ', disciplineVisited.id)
                print('Disciplina Visitada PERIODO: ', disciplineVisited.timeCourse)
                print('Disciplina Visitada DEPENDENCIA: ', disciplineVisited.dependencies)
                print('Punições: ', totalPunishments)
                print('------')
                
        disciplineVisitedList.append(discipline)

    return totalPunishments


def teacherScheduleConflict(discipleneList: List[Discipline]):
    """Verifica se professor não está dando aula em duas ou mais materias ao mesmo tempo"""

    totalPunishments: int = 0

    for discipline in discipleneList:
        for currentDiscipline in discipleneList:

            print('------')
            print('Disciplina Lista: ', discipline.id)
            print('Disciplina Lista Posição: ', discipline.positions)
            print('Disciplina Lista Professor: ', discipline.teacher)
            print('')
            print('Disciplina Atual: ', currentDiscipline.id)
            print('Disciplina Lista Posição: ', currentDiscipline.positions)
            print('Disciplina Atual Professor: ', currentDiscipline.teacher)
            print('Punições: ', totalPunishments)
            print('------')

            if discipline.teacher == currentDiscipline.teacher and discipline.name != currentDiscipline.name:
                for position in discipline.positions:
                    if position in currentDiscipline.positions:
                        totalPunishments = totalPunishments + Punishments.teacherScheduleConflict
    
    return totalPunishments

def calculatePopulationFitness(populations: List[Discipline]):
    for population in populations:

        totalPunishmentsClassesOverlap = classesOverlap(population)
        # totalPunishmentsDisorderedDependencies = disorderedDependencies(population)
        totalPunishmentsTeacherScheduleConflict = teacherScheduleConflict(population)

        print('Disciplinas SOBREPOSICAO: ', totalPunishmentsClassesOverlap)
        # print('Disciplinas DESORDENADAS: ', totalPunishmentsDisorderedDependencies)
        print('Disciplinas PROFESSOR: ', totalPunishmentsTeacherScheduleConflict)
