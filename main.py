from typing import List
from controller.createPopulation import createPopulation
from model.population import Population
from model.utils.constants import INITIAL_POPULATION, MAX_NUMBER_TIME_CORSE
from model.chromosome import Chromosome
from controller.utils.readFile import readFile
from controller.utils.validatorDisciplines import calculatePopulationFitness

chromosome: Chromosome = readFile('database/disciplinas_1_4_utfpr_sh.json')
populations: Population = createPopulation(chromosome)


calculatePopulationFitness(populations)
print('Populations: ', populations.id)
