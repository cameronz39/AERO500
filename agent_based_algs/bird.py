import numpy as np
import random

class Bird():
    def __init__(self,a):
        self.a = a # half of a birds wingspan
        self.r = np.array([[random.uniform(-10,10)],[random.uniform(-10,10)]])