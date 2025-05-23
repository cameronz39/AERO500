import numpy as np
import random

values_0  = [23, 21, 8, 1, 3, 7, 18, 19, 17, 15, 24, 22, 6, 28, 4, 2, 27, 20, 5, 10]
weights_0 = [7,  2,  6, 9, 1, 5,  6,  1,  3,  4,  7,  9, 3,  7, 3, 4,  5,  1, 5,  4]
MAX_WEIGHT = 45

class Chromosome:

    def __init__(self, numGenes = 20):
        self.genes = random.choices([0, 1], k = numGenes)
        self.fitness = 0

    def mutate(self):
        # Implement random mutation
        rand_index = random.randint(0,len(self.genes) - 1)
        self.genes[rand_index] = 1 - self.genes[rand_index]

    def __add__(self, o):
        # Implement single point crossover with random crossover point
        rand_index = random.randint(0,len(self.genes) - 1)
        child = Chromosome(20)
        child.genes = self.genes[:rand_index] + o.genes[rand_index:]
        return child
    
class Population:

    def __init__(self, populationSize, numGenes = 20):
        self.members = [Chromosome(numGenes) for i in range(populationSize)]

    def selection(self, ratio):
        # Implement Selection
        # Step 1 - Sort members by fitness
        self.members.sort(key=lambda x:x.fitness, reverse=True)
        # Step 2 - return some number of members based on the ratio provided
        cutoff_index = int(len(self.members) * ratio)
        return self.members[:cutoff_index]

def myFitnessFunction(chrom: Chromosome):
    indicies = []
    for i in range(len(chrom.genes)):
        if chrom.genes[i]: indicies.append(i)

    total_weight = sum([weights_0[i] for i in indicies])
    total_val = sum([values_0[i] for i in indicies])

    if total_weight > MAX_WEIGHT:
        chrom.fitness = 0
    else:
        chrom.fitness = total_val