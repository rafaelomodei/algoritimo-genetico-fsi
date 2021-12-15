
import copy
import random
from typing import List
from model.chromosome import Chromosome
from model.population import Population
from model.punishments import Punishments
from model.discipline import Discipline
from model.utils.constants import INITIAL_POPULATION, MASK_CROSSOVER, MAX_NUMBER_TIME_CORSE

def classesOverlap(chromosome: Chromosome) -> int:
    """Verifica se a disciplina atual tem conflito de horario com outra disciplina"""
    """Verificar se a disciplina do mesmo periodo está ocupando o mesmo horario de outra disciplina"""

    totalPunishments: int = 0
    positionsOccupied: list[int] = list()

    for discipline in chromosome.disciplineList:
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

def disorderedDependencies(chromosome: Chromosome) -> int:
    """Verifica se as dependências estão desordenadas... exem: calculo 2 vim antes de calculo 1"""

    totalPunishments: int = 0
    disciplineVisitedList: List[Discipline] = list()

    for discipline in chromosome.disciplineList:
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


def teacherScheduleConflict(chromosome: Chromosome) -> int:
    """Verifica se professor não está dando aula em duas ou mais materias ao mesmo tempo"""

    totalPunishments: int = 0

    for discipline in chromosome.disciplineList:
        for currentDiscipline in chromosome.disciplineList:

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


def calculateChromosomeFitness(penalty:  int) -> float:
    """Calcula o valor do fitness do cromossomo"""

    fitness = 100 /  100 + penalty
    return fitness 

def assessChromosomeFitness(chromosome: Chromosome) -> float:
    """Avalia o fitnes do cromossomo"""

    totalPunishmentsClassesOverlap = classesOverlap(chromosome)
    # totalPunishmentsDisorderedDependencies = disorderedDependencies(chromosome)
    totalPunishmentsTeacherScheduleConflict = teacherScheduleConflict(chromosome)
    
    chromosome.penalty = calculateChromosomeFitness(totalPunishmentsClassesOverlap + totalPunishmentsTeacherScheduleConflict)
    
    print('Disciplinas SOBREPOSICAO: ', totalPunishmentsClassesOverlap)
    # print('Disciplinas DESORDENADAS: ', totalPunishmentsDisorderedDependencies)
    print('Disciplinas PROFESSOR: ', totalPunishmentsTeacherScheduleConflict)
    print('Penalidade: ', chromosome.penalty)
    return chromosome.penalty


def assessPopulation(population: Population) -> Population:
    """Avalia a população"""

    PopulationFitness = 0

    for chromosome in population.populationsList:
        print('>> ID: ', chromosome.id)
        PopulationFitness = PopulationFitness + assessChromosomeFitness(chromosome)
    
    population.penalty = PopulationFitness

    return population


def createRoulette(population: Population) -> Population:
    """Cria roleta"""

    rollette: Population = Population(0)
    rollette.id = population.id + 1
    rollette.populationsList = []

    print('-----')
    print('Chomossomos criado na roleta')
    for chromosome in population.populationsList:
        #Calcula quantos porcento o chromosome ocupa a roleta
        percentage = ((chromosome.penalty * 100) / population.penalty)
        print('ID: ', chromosome.id, ' | percentage', round(percentage), ' | Penalidade: ', chromosome.penalty )

        for x in range(round(percentage)):
            rollette.populationsList.append(chromosome)
    
    print('Total de chomossomos na população: ', len(population.populationsList))
    print('Total de chomossomos na roleta: ', len(rollette.populationsList))
    print('-----')

    return rollette

def selectChromosomesInRoulette(rollette: Population) -> Population:
    """Seleciona o chomossomo que está na roleta"""

    selectedChromosomes: Population = Population(0)
    selectedChromosomes.populationsList = []

    totalChromosomesSelected: int = round((INITIAL_POPULATION * 100) / len(rollette.populationsList))

    for x in range(totalChromosomesSelected):
        chromosome = random.choice(rollette.populationsList)
        selectedChromosomes.populationsList.append(chromosome)


    print('Chomossomos selecionados na roleta')
    for chromosome in selectedChromosomes.populationsList:
        print('ID: ', chromosome.id, ' | Penalidade: ', chromosome.penalty )
    
    print('-----')

    return selectedChromosomes

def crossover(population: Population) -> Population:

    father: Population = copy.deepcopy(population)
    mom: Population = copy.deepcopy(population)
    children: Chromosome = Chromosome([])
    childrenPopulation: Population = Population(0)
    childrenPopulation.populationsList = []
    toogle: bool = False

    for x in range(len(population.populationsList)):
        print('--------')
        print('X: ', x)
        print('father.populationsList LEN: ', len(father.populationsList))
        print('father.disciplineList LEN: ', len(father.populationsList[x].disciplineList))
        print('mom.populationsList LEN: ', len(mom.populationsList))
        print('mom.disciplineList LEN: ', len(mom.populationsList[x].disciplineList))
        print('MASK_CROSSOVER LEN: ', len(MASK_CROSSOVER))
        print('--------')

        while len(childrenPopulation.populationsList[x].disciplineList) <= len(population.populationsList[x].disciplineList):
            if toogle:
                childrenPopulation.populationsList[x].disciplineList.append(father.populationsList[x].disciplineList.pop())
            else:
                childrenPopulation.populationsList[x].disciplineList.append(mom.populationsList[x].disciplineList.pop())



        # mask = copy.deepcopy(MASK_CROSSOVER)
        # currentPosition = 0
        # for discipline in population.populationsList[x].disciplineList:
        #     toggle = mask.pop() 
        #     print('MASK_CROSSOVER: ', toggle)
        #     if toggle:
        #         for position in father.populationsList[x].disciplineList:
        #             if position == currentPosition:

        #                 # print('Disciplina: ', father.populationsList[x].disciplineList[len(father.populationsList[x].disciplineList) -1].name)
        #                 # children.disciplineList.append(father.populationsList[x].disciplineList.pop())
        #                 print('father.disciplineList LEN: ', len(father.populationsList[x].disciplineList))
        #                 print('mom.disciplineList LEN: ', len(mom.populationsList[x].disciplineList))
        #                 print('')
        #                 children.disciplineList.append(father.populationsList[x].disciplineList.pop())
        #                 mom.populationsList[x].disciplineList.pop()
        #     else:
        #         print('father.disciplineList LEN: ', len(father.populationsList[x].disciplineList))
        #         print('mom.disciplineList LEN: ', len(mom.populationsList[x].disciplineList))
        #         print('')

        #         children.disciplineList.append(mom.populationsList[x].disciplineList.pop())
        #         father.populationsList[x].disciplineList.pop()

        #     childrenPopulation.populationsList.append(children)

    print('Tamanho do filho: ', len(childrenPopulation.populationsList))


    for discipline in children.disciplineList:
        print('Nome da disciplina: ', discipline.name, ' | Periodo: ', discipline.timeCourse, ' | Posição: ', discipline.positions)

    # for chromosomeFather in father.populationsList:

        # print('Quantidade de disciplina: ', len(father.populationsList[x].disciplineList))
        # for x in range(round(len(chromosomeFather.disciplineList)/5)):
        #     print('Chomossomo PAI: ', chromosomeFather.disciplineList[len(chromosomeFather.disciplineList) -1].name, ' | [i]: ', i)
        #     children.disciplineList.append(chromosomeFather.disciplineList.pop())
      

        # i = i + 1





    # for x in range(len(population.populationsList)):
    #     mask = copy.deepcopy(MASK_CROSSOVER)
    #     toggle = mask.pop()
    #     if toggle:
    #         for discipline in father.populationsList[x].disciplineList:
    #             children.disciplineList.append(discipline)
    #             print('Chomossomo PAI: ', discipline.name, ' | [i]: ', i)
    #     else:
    #         for discipline in mom.populationsList[x].disciplineList:
    #             children.disciplineList.append(discipline)
    #             print('Chomossomo MÃE: ', discipline.name, ' | [i]: ', i)
            
    #     i = i + 1
    
    print('>>>>>>')
        # print('Nome da disciplina: ', children.disciplineList)
    


