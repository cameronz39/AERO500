from copy import deepcopy
import numpy as np

class Event():
    def __init__(self,id,t_start,duration,val):    
        self.id = id
        self.t_start = t_start
        self.duration = duration
        self.val = val
    def t_end(self):
        return self.t_start + self.duration

events = []
events.append(Event(0,12,4,5))
events.append(Event(1,3,4,8))
events.append(Event(2,7,2,8))
events.append(Event(3,21,3,9))
events.append(Event(4,23,3,5))
events.append(Event(5,24,1,7))
events.append(Event(6,1,3,5))
events.append(Event(7,17,2,6))
events.append(Event(8,13,1,6))
events.append(Event(9,20,4,5))

events_sorted = []
while events: # sort events by start time
    min_idx = 0
    for i in range(1, len(events)):
        if events[i].t_start < events[min_idx].t_start:
            min_idx = i
    events_sorted.append(events.pop(min_idx))

all_scheds: list[list[Event]] = [[]] # list of lists of events

for e in events_sorted:

    new_scheds = []
    for sched in all_scheds:
        if len(sched) == 0: # always keep the empty schedule
            sched_copy = deepcopy(sched)
            sched.append(e)
            new_scheds.append(sched_copy)
    
        elif (e.t_start >= sched[-1].t_end()):  # else go into DSP algorithm
            sched_copy = deepcopy(sched)
            sched.append(e)
            new_scheds.append(sched_copy)

    all_scheds.extend(new_scheds)

values = []
for sched in all_scheds:
    values.append(sum(e.val for e in sched))

# find and save the best schedule
max_idx = np.argmax(np.asarray(values))

print(f"Maximum total value = {values[max_idx]}")
print("Event ids in best schedule: ", [e.id for e in all_scheds[max_idx]])