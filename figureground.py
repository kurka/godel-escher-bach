# -*- coding: utf-8 -*-
"""
@author: kurka
"""

f = 1 #initial figure value
g = 0 #initial ground value
queue = [1] #queue with relevant figure values

print f
for i in range(10): #set here how many iterations the program should run
    if queue[0] != g+1: #if next ground isnt in figure set
        g += 1
    else:
        g += 2
        queue.pop(0)
        
    f += g
    queue.append(f)
    #print g
    print f
    
