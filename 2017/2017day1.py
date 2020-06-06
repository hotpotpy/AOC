# -*- coding: utf-8 -*-
"""
@author: Aaron
"""
#%%
print("----------------------------")
print("Advent of Code 2017, Day 1")
print("----------------------------")
#%%
import sys

if len(sys.argv) == 1:
    file = 'input_day1.txt'
else:
    file = sys.argv[1]

with open(file,'r') as f:
    data = f.read()
#%%
data = data.replace('\n','')
#%%
def captcha_sum(string,steps):
    num_list = []
    for i in range(0,len(string)):
        if data[i] == data[i - steps]:
            num_list.append(string[i])
    num_list = [int(num) for num in num_list]
    sum_list = sum(num_list)
    return sum_list
#%%
ans1 = captcha_sum(data,1)
print("Answer to part 1: " + str(ans1))
ans2 = captcha_sum(data,int(len(data)/2))
print("Answer to part 2: " + str(ans2))
# #%%
# num_list = []
# for i in range(0,len(data)):
#     if data[i] == data[i-1]:
#         num_list.append(data[i])

# num_list = [int(num) for num in num_list]
# ans1 = sum(num_list)
# print("Answer to part 1: " + str(ans1))
# #%%

# num_list2 = []
# skip_len = int(len(data)/2)
# for i2 in range(0,len(data)):
#     if data[i2] == data[i2-skip_len]:
#         num_list2.append(data[i2])
# num_list2 = [int(num) for num in num_list2]
# ans2 = sum(num_list2)
# print("Answer to part 2: " + str(ans2))