import random

values_0 = [23, 21, 8, 1, 3, 7, 18, 19, 17, 15, 24, 22, 6, 28, 4, 2, 27, 20, 5, 10] # $
weights_0 = [7, 2, 6, 9, 1, 5, 6, 1, 3, 4, 7, 9, 3, 7, 3, 4, 5, 1, 5, 4] # kg
MAX_WEIGHT = 45

best_value = 0
best_weight = 0

best_indicies = []


maxIterations = 100000
for i in range(1, maxIterations + 1):

    # randomly add items to the knapsack
    values = values_0.copy()
    weights = weights_0.copy()
    n = len(values)-1
    indicies = [] 
    curr_value = 0
    curr_weight = 0

    while True:
        rand_index = random.randint(0,n)
        if curr_weight + weights[rand_index] > MAX_WEIGHT:
            break
        else:
            curr_weight += weights.pop(rand_index)
            curr_value += values.pop(rand_index)
            n = n - 1
            indicies.append(rand_index)

    final_knapsack = [weights_0[i] for i in indicies]
    
    if curr_value > best_value:
        best_value = curr_value
        best_weight = curr_weight
        best_indicies = indicies

    
print(f"Current best value: {best_value}")

print(f"Weight {best_weight}, Value: {best_value} with items:")  
print(final_knapsack)
