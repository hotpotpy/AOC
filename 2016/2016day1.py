# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 21:40:23 2020

@author: Aaron
"""
#%%
print("----------------------------")
print("Advent of Code 2016, Day 1")
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
directions = data.split(', ')
directions[-1] = directions[-1].replace('\n','')
"""
north: right x+, left x-
south: right x-, left x+
west: right y+, left y-
east: right y-, left y+
"""
#%%
class object():
    def __init__(self, x, y, facing):
        self.x = x
        self.y = y
        self.dic = {x:{y:0}}
        self.twice_flag = False
        self.position_twice = None
        self.facing = facing
    def move(self,start, stop, axis, final):
        # Track movement across grid
        # Ex: at (5,5), if start = 5,stop=8,axis='x',final=8
        # Updates self.dic, +1 to:
        # self.dic[6][5],self.dic[7][5]
        # then self.dic[8][5] because 8 is final (moving 5 to 8)
        if axis == 'y':
            for i in range(start+1, stop):
                if i not in self.dic[self.x].keys():
                    self.dic[self.x][i] = 1
                else:
                    self.dic[self.x][i] += 1
                    self.check_pos_twice(self.x,i)
            self.y = final
            if self.y not in self.dic[self.x].keys():
                self.dic[self.x][self.y] = 1
            else:
                self.dic[self.x][self.y] += 1
            self.check_pos_twice(self.x,self.y)
        elif axis == 'x':
            for i in range(start+1, stop):
                if i not in self.dic.keys():
                    self.dic[i] = {}
                    self.dic[i][self.y] = 1
                else:
                    if self.y not in self.dic[i].keys():
                        self.dic[i][self.y] = 1     
                    else:
                        self.dic[i][self.y] += 1
                    self.check_pos_twice(i,self.y)
            self.x = final
            if self.x not in self.dic.keys():
                self.dic[self.x] = {self.y: 1}
            else:
                if self.y not in self.dic[self.x].keys():
                    self.dic[self.x][self.y] = 1
                else:
                    self.dic[self.x][self.y] += 1
            self.check_pos_twice(self.x,self.y)
    def check_pos_twice(self,x,y):
        if self.twice_flag == True:
            return None
        else:
            if self.dic[x][y] > 1:
                self.position_twice = [x, y]
                self.twice_flag = True
            else:
                return None
                
        
#%%
"""
north: right x+, left x-
south: right x-, left x+
west: right y+, left y-
east: right y-, left y+
"""
#%%
obj = object(0,0,'N')
for step in directions:
    turn = step[0]
    num = int(step[1:])
    if obj.facing == 'N':
        if turn == 'L': 
            obj.move(obj.x-num,obj.x,'x',obj.x-num)
            #position[0] -= num
            obj.facing = 'W'
        elif turn == 'R': 
            #position[0] += num
            obj.move(obj.x,obj.x+num,'x',obj.x+num)
            obj.facing = 'E'
        else: 
            raise SystemExit
    elif obj.facing == 'S':
        if turn == 'L': 
            #position[0] += num
            obj.move(obj.x,obj.x+num,'x',obj.x+num)
            obj.facing = 'E'
        elif turn == 'R': 
            #position[0] -= num
            obj.move(obj.x-num,obj.x,'x',obj.x-num)
            obj.facing = 'W'
        else: 
            raise SystemExit
    elif obj.facing == 'W':
        if turn == 'L':
            #position[1] -= num
            obj.move(obj.y-num,obj.y,'y',obj.y-num)
            obj.facing = 'S'
        elif turn == 'R':
            #position[1] += num
            obj.move(obj.y,obj.y+num,'y',obj.y+num)
            obj.facing = 'N'
        else:
            raise SystemExit
    elif obj.facing == 'E':
        if turn == 'L':
#            position[1] += num
            obj.move(obj.y,obj.y+num,'y',obj.y+num)
            obj.facing = 'N'
        elif turn == 'R':
            #position[1] -= num
            obj.move(obj.y-num,obj.y,'y',obj.y-num)
            obj.facing = 'S'
        else:
            raise SystemExit
    
#%%
ans1 = abs(obj.x) + abs(obj.y)
ans2 = abs(obj.position_twice[0]) + abs(obj.position_twice[1])

print("Answer to Part One: " + str(ans1))
print("Answer to Part Two: " + str(ans2))
