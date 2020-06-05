#%%
print("----------------------------")
print("Advent of Code 2015, Day 3")
print("----------------------------")
#%%
import sys

if len(sys.argv) == 1:
    file = 'input_day3.txt'
else:
    file = sys.argv[1]

with open(file,'r') as f:
    data = f.read()
#%% PART ONE

# Initialize grid dictionary
dic = {0:{0:1}}
x = 0
y = 0

for step in data:
    if step == '^':
        y += 1
    elif step == 'v':
        y -= 1
    elif step == '>':
        x += 1
    elif step == '<':
        x -= 1
    if x not in dic.keys():
        dic[x] = {}
    if y not in dic[x].keys():
        dic[x][y] = 0
    dic[x][y] += 1
#%%
count = 0
for xkey in dic.keys():
    count += len(dic[xkey])

print("Answer to Part One: " + str(count))
#%% PART TWO

# Initialize grid dictionary
dic2 = {0:{0:2}}
x1, y1 = 0, 0
x2, y2 = 0, 0

for i in range(0,len(data)):
    step = data[i]
    move_x, move_y = 0, 0
    if step == '^':
        move_y = 1
    elif step == 'v':
        move_y = -1
    elif step == '>':
        move_x = 1
    elif step == '<':
        move_x = -1
    if i % 2 == 0:
        x1 += move_x
        y1 += move_y
        upd_x = x1
        upd_y = y1
    else:
        x2 += move_x
        y2 += move_y
        upd_x = x2
        upd_y = y2
    if upd_x not in dic2.keys():
        dic2[upd_x] = {}
    if upd_y not in dic2[upd_x].keys():
        dic2[upd_x][upd_y] = 0
    dic2[upd_x][upd_y] += 1
#%%
count2 = 0
for xkey2 in dic2.keys():
    count2 += len(dic2[xkey2])

print("Answer to Part Two: " + str(count2))