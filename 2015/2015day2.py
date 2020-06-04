# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 19:27:44 2020

@author: Aaron
"""

#%%
print("----------------------------")
print("Advent of Code 2015, Day 2")
print("----------------------------")
#%%
import sys

if len(sys.argv) == 1:
    file = 'input_day2.txt'
else:
    file = sys.argv[1]

with open(file,'r') as f:
    data = f.read()
#%%
tot_paper = 0
tot_ribbon = 0
data = data.split('\n')
if data[-1] == '':
    del data[-1]
    
for i in range(0,len(data)):
    box = data[i]
    dims = box.split('x')
    dims = [int(dim) for dim in dims]
    # Wrapping paper
    areas = [dims[0]*dims[1],dims[1]*dims[2],dims[0]*dims[2]]
    min_area = min(areas)
    tot_wrap = sum(areas * 2) + min_area
    tot_paper += tot_wrap
    # Ribbon
    bow = dims[0]*dims[1]*dims[2]
    wrap = sorted(dims)[0:2]
    wrap = wrap[0]*2+wrap[1]*2
    tot_ribbon += bow + wrap

print("Answer to Part One: " + str(tot_paper))
print("Answer to Part Two: " + str(tot_ribbon))

    
