import random
import matplotlib.pyplot as plt
import numpy as np
from collections import deque

plt.figure()
inside_pts = 0 
last_estimate = 0
current_estimate = 0
tol = 0.005
maxIterations = 5000
past_diffs = deque(maxlen=5) # queue of the 5 previous differences
for i in range(1,maxIterations+1):
    rand_x = random.uniform(-2, 3) # domain of integration
    rand_y = random.uniform(0, 10) # enough to safely capture the range of the function on this domain
    
    col = 'blue'
    if rand_y <= (rand_x**3)*np.sin(rand_x): # if point is inside function
        inside_pts += 1
        col = 'red' 
    plt.scatter(rand_x,rand_y,color=col)
    
    # the ratio of points inside the function to total points should equal 
    # the ratio of area under the curve to total area
    current_estimate = (5*10)*(inside_pts / i) 
    if i != 0:
        past_diffs.append(abs(current_estimate - last_estimate))   

        # only break if we are certain the differences are settling
        if len(past_diffs) == 5 and all(d < tol for d in past_diffs):
            break
    last_estimate = current_estimate

x = np.linspace(-2,3,100)
y = (x**3)*np.sin(x)
plt.plot(x,y,color='black',linewidth=3)
plt.title("Integration using the Monte Carlo Method")
plt.show()
print(f"Estimate using Monte Carlo Integration method: {last_estimate} with {i} points")