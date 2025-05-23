import GA
import random
import numpy as np
import matplotlib.pyplot as plt

SELECTION_RATIO = 0.85
MUTATION_RATE = 0.1
POP_SIZE = 20
NUM_GENERATIONS = 50

avg_fitness_hist = []
best_fitness_hist = []
# Step 1 - Initialize Population
myPop = GA.Population(populationSize = POP_SIZE, numGenes = 20)

for i in range(1,NUM_GENERATIONS):
    for c in myPop.members: # updates the fitness of each chromosome
        GA.myFitnessFunction(chrom=c) 

    avg_fitness = np.mean([c.fitness for c in myPop.members])
    avg_fitness_hist.append(avg_fitness)

    best_fitness = max([c.fitness for c in myPop.members])
    best_fitness_hist.append(best_fitness)

    # Step 2 - Selection 
    fittest = myPop.selection(SELECTION_RATIO) # keeps only the fittest members

    # Step 3 - Crossover and Mutate
    new_gen = []
    while len(new_gen) < POP_SIZE: # repeat so population does not drop
        parent1 = random.sample(fittest,1) # sample two of the fittest parents
        parent2 = random.sample(fittest,1)
        child = parent1[0] + parent2[0] # crossover
        
        if random.random() <= MUTATION_RATE:
            child.mutate()

        new_gen.append(child)

    # Step 4 - repeat
    myPop.members = new_gen




plt.figure()
plt.plot(best_fitness_hist)
plt.xlabel("Generation Number")
plt.ylabel("Best Fitness")
plt.title("Best Population Fitness over time")
plt.grid()

plt.figure()
plt.plot(avg_fitness_hist)
plt.xlabel("Generation Number")
plt.ylabel("Average Fitness")
plt.title("Average Population Fitness over time")
plt.grid()
plt.show()
