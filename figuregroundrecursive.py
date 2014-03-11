# -*- coding: utf-8 -*-
"""
@author: kurka
"""

def figure(n):
    if n == 1:
        return 1
    else:
        return figure(n-1) + ground(n-1)
        
def ground(n):
    if n == 1:
        return 2
    else:   
        prev_ground = ground(n-1) #solve this only once!
        for i in range(1,n+1):            
            if figure(i) == prev_ground+1:
                return prev_ground + 2
        return prev_ground + 1