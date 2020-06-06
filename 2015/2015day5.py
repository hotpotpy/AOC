# -*- coding: utf-8 -*-
"""
@author: Aaron
"""
#%%
print("----------------------------")
print("Advent of Code 2015, Day 5")
print("----------------------------")
#%%
import sys

if len(sys.argv) == 1:
    file = 'input_day5.txt'
else:
    file = sys.argv[1]

with open(file,'r') as f:
    data = f.read()
#%%
lines = data.split('\n')
if lines[-1] == '':
    del lines[-1]
    
counter = 0
vowels = ['a','e','i','o','u']

for string in lines:
    # Rule 3
    # If not satisfied, skip line
    if ('ab' in string) or ('cd' in string) or ('pq' in string) or ('xy' in string):
        continue
    # Rule 2
    consec = False
    for i in range(0,len(string)-1):
        if string[i] == string[i+1]:
            consec = True
            break
    if consec == False:
        continue
    # Rule 1
    vowel_cnt = 0
    for vowel in vowels:
        vowel_cnt += string.count(vowel)
    if vowel_cnt < 3:
        continue
    counter += 1
print("Answer to part 1: " + str(counter))
#%% PART TWO

counter2 = 0
for string2 in lines:
    # Check rule 2 by iterating each line content
    rule2 = False
    for i2 in range(0,len(string2)-2):
        if string2[i2] == string2[i2+2]:
            rule2 = True
            break
    # If rule 2 not satisfied, go to next line
    # Rule 1 doesn't need to be checked        
    if rule2 == False:
        continue
    # Check rule 1 using dictionary
    dic = {}
    prev_prev_pair = None
    prev_pair = None
    for i3 in range(0,len(string2)-1):
        pair = string2[i3] + string2[i3+1]
        # Add to dic if pair doesn't exist
        if pair not in dic.keys():
            dic[pair] = 1
        # for the case of three consecutive letters
        elif pair == prev_pair and pair != prev_prev_pair:
            pass
        # if pair exists in dic then value must be > 1, which passes rule 1
        else:
            dic[pair] += 1
            counter2 += 1
            break
        prev_prev_pair = prev_pair
        prev_pair = pair
print("Answer to part 2: " + str(counter2))