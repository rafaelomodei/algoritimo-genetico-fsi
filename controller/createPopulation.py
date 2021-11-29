import copy
from model.chromosome import Chromosome
from controller.createChromosomes import createChromosomes
from model.population import Population
from model.utils.constants import INITIAL_POPULATION

def createPopulation(chromosome: Chromosome) -> Population:
    populations: Population = Population(0)

    populations.id = populations.id + 1
    populations.populationsList = []


    for newChromosome in range(INITIAL_POPULATION):
        
        currentChromosome: Chromosome = createChromosomes(copy.deepcopy(chromosome))
        currentChromosome.id = newChromosome + 1 # add 1 para ter o id apartir do numero 1
        populations.populationsList.append(currentChromosome)

        for discipline in currentChromosome.disciplineList:
            print(
                'ID: ', discipline.id,
                'Nome: ', discipline.name,
                'Professor: ', discipline.teacher,
                'Horas semanais: : ', discipline.weeklyWorkload,
                'Posições: ', discipline.positions,
                'Dependencia: ', discipline.dependencies,
                'Periodo: ', discipline.timeCourse,
            )
    
    return populations