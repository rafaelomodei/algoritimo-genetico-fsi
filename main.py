import copy
from typing import List
from createFistPopulation import createFistPopulation
from utils.constants import INITIAL_POPULATION, MAX_NUMBER_TIME_CORSE
from discipline import Discipline
from readFile import readFile
from createChromosomes import createChromosomes
from utils.validatorDisciplines import calculatePopulationFitness

chromosomesList: List[Discipline] = readFile('disciplinas_1_4_utfpr_sh.json')
populations: List[List[Discipline]] = createFistPopulation(chromosomesList)

calculatePopulationFitness(populations)
