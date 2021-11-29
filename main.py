from typing import List
from controller.createPopulation import createPopulation
from model.population import Population
from model.utils.constants import INITIAL_POPULATION, MAX_NUMBER_TIME_CORSE
from model.chromosome import Chromosome
from controller.utils.readFile import readFile
from controller.utils.validatorDisciplines import assessPopulation, createRoulette, selectChromosomesInRoulette

chromosome: Chromosome = readFile('database/disciplinas_1_4_utfpr_sh.json')
population: Population = createPopulation(chromosome)


currentPopulation: Population = assessPopulation(population)
print('Populations ID: ', population.id)
print('Populations PUNIÇÃO: ', population.penalty)




selectChromosomesInRoulette(createRoulette(currentPopulation))
