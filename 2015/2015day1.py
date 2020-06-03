# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 00:58:01 2020

@author: Aaron
"""
#%% PART ONE and PART TWO
file = 'input_day1.txt'
with open(file,'r') as f:
    data = f.read()

# Counter for part one
counter = 0
# Indicator for part two
# Only need to know first time counter < 0 (basement)
bsmt_first = False
for n, char in enumerate(data):
    if char == '(':
        counter += 1
    elif char == ')':
        counter -=1
    else:
        print("Error")
        raise SystemExit
    # Add plus 1 because question starts counting at 1
    # but enumerate starts at 0
    if bsmt_first == False and counter == -1:
        print("PART TWO: " + str(n+1))
        bsmt_first = True
print("PART ONE: " + str(counter))

