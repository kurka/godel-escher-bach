# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 10:16:07 2014

@author: David Kurka
"""

#Trying to solve the MU puzzle, proposed by Douglas Hoefstadter in
# Godel, Escher, Bach book, *using brute force!* (mechanical mode)

#MU puzzle:

#start with MI
#rule 1: xI -> xIU
#rule 2: Mx -> Mxx
#rule 3: xIIIy -> xUy
#rule 4: xUUy -> xy
#try to get MU

import re


theorems_collection = [] #store the theorems already analysed
theorems_queue = ['MI'] #store the theorems to be analysed

def check_and_insert(new_theorem):
    if new not in theorems_collection and new not in theorems_queue: #check if theorem already exists
        theorems_queue.append(new) #insert it in the queue
            
    
for i in range(1, 10000): #change the range with caution! your computer may overload!
    #get the shortest string to apply the rules
    #theorems_queue.sort()
    theorems_queue.sort(key=len)
    current = theorems_queue.pop(0)
    print("Current theorem: %s" %current)
    
    if current == 'MU':
        print("MU LOCATED!!!")
        break
    
    #try to apply rule 1:  xI -> xIU
    if current[-1] == 'I':
        new = current + 'U'
        check_and_insert(new)
       
    
    #apply rule 2: Mx -> Mxx
    new = 'M' + current[1:]*2
    check_and_insert(new)
    
    #try to apply rule 3: xIIIy -> xUy
    three_i = (m.start() for m in re.finditer('(?=III)', current))
    for i in three_i:
        new = current[:i] + 'U' + current[i+3:]
        check_and_insert(new)
        
    #try to apply rule 4: xUUy -> xy
    two_u = (m.start() for m in re.finditer('(?=UU)', current))
    for i in two_u:
        new = current[:i] + current[i+2:]
        check_and_insert(new)
        
    
    
    
    #add current theorem to the collection    
    theorems_collection.append(current)
    
    

        

