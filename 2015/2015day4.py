# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 16:55:36 2020

@author: Aaron
"""

print("----------------------------")
print("Advent of Code 2015, Day 4")
print("----------------------------")
#%%

#code = 'abcdef609043'
code = 'ckczppom'
# bit_list = []
# for char in code:
#     bit_list.append(format(ord(char),'b').zfill(8))
# bit = ''.join(bit_list)

# num_pad = 448 - len(bit) % 512

# step1 = bit + '1' + '0' * (num_pad - 1)
# step1 += format(len(bit),'b').zfill(64)
# #%%
# A = '01234567'
# B = '89abcdef'
# C = 'fedcba98'
# D = '76543210'

import hashlib
i = 0
while True:
    code1 = code + str(i)
    string = code1.encode('utf-8')
    result = hashlib.md5(string).hexdigest()
    if result[0:5] == '00000':
        ans1 = code1
        break
    else:
        i += 1
#%%
print("Answer to part 1: " + str(ans1))
#%%
i2 = 0
while True:
    code2 = code + str(i2)
    string = code2.encode('utf-8')
    result2 = hashlib.md5(string).hexdigest()
    if result2[0:6] == '000000':
        ans2 = code2
        break
    else:
        i2 += 1        
#%%
print("Answer to part 2: " + str(ans2))