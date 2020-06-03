# -*- coding: utf-8 -*-
"""
@author: Aaron
"""
#%%
print("----------------------------")
print("Advent of Code 2019, Day 1")
print("----------------------------")
#%%
import sys
import numpy as np

if len(sys.argv) == 1:
    file = 'input_day1.txt'
else:
    file = sys.argv[1]

with open(file,'r') as f:
    lines = f.readlines()
    
lines = [line.replace('\n','') for line in lines]

series = np.array(lines, dtype=int)

part1_ans = sum(series // 3 - 2)
print("Answer to Part One: " + str(part1_ans))
#%% PART TWO
total = 0
for num in series:
    fuel = num
    while True:
        fuel = fuel // 3 - 2
        if fuel <= 0:
            break
        total += fuel
print("Answer to Part Two: " + str(total))