

from collections import defaultdict
from typing import List
#
# class Launch:
#     def __init__(self):
#         self.checkInMap = {} # this map id ---> (time, station)
#         self.checkOutMap = {} # this map (StartingStation,endingStation)---> [diff(timeOut - timeIn),count]
#
#     def checkIn(self,id:int, station:str,time:int)->None:
#         self.checkInMap[id] = (time ,station)
#         # add map the id of the person to the station and the time he got into the station
#
#
#     def checkOut(self,id:int,outStation:str,t:int)->None:
#         (startinStation,startingTime) = self.checkInMap[id]
#         # check if this path has been traveling befere this user
#         if(startinStation,outStation) not in self.checkOutMap:
#             self.checkOutMap[(startinStation,outStation)] = [(0,0)]
#
#         # Now since the path have been traveling before i can just add the the time diff and the count++
#         self.checkOutMap[(startinStation,outStation)][0] += t - startingTime
#         self.checkOutMap[(startinStation,outStation)][1] += 1 
#
#     def getAverageTime(self,startStation:str,endStation:str)->float:
#         allTime, count = self.checkOutMap[(startStation,endStation)]
#         return allTime / count



# class Node:
#     def __init__(self,val,prev,next,child):
#         self.val = val
#         self.prev = prev
#         self.next = next
#         self.child = child
#
    
# class Solution:
#     def flatten(self,head:Node)->Node:
#         temp = head
#         stack = []
#         # as long as the head has has a connection we run this loop
#             # if the head has a child:
#                 # if the head.child is not None
#                 # put the next node in the stack
#                 # then the child becomes the head.next
#                 # then the head.next.prev become the head
#                 # then the child becomes None
#             # in case the head has no child and the the stack is not empty
#                 # get the Node from the stack and the head.next= to that  new Node
#                 # then the head.next.prev is equal to the head
#         #the head = head.next
#
#         while head != None:
#             if head.child != None:
#                 if head.next != None:
#                     stack.append(head.next)
#                 head.next = head.child
#                 head.next.prev = head
#                 head.child = None
#             else:
#                 if head.child == None and len(stack):
#                     head.next = stack.pop()
#                     head.next.prev = head
#             head = head.next
#         return temp
#

# class Sea:
#     def hasShips(self,topRight:'Point',bottomLeft:'Point')->bool:
#         return False 
#
#
# class Point:
#     def __init__(self,x:int,y:int):
#         self.x = x
#         self.y = y
#
# # the work we have to do is to find all the ships that are present a in big rectangle
# # but what we can do is to divide the bigger rectange into mulitple rectangle
# class Solution:
#     def __init__(self):
#         pass
#
#     def countShips(self,sea:'Sea',topRight:'Point',bottomLeft:'Point')->int:
#         # first we need to check if the input top right and bottomLeft of the rectangle as a ship.
#         # by using the function hasShips(topR,botLef)->bool.
#         # initialize the count to zero.
#         # if the rectangle has at least one ship?
#             # count that and then move to the next position buy going 
#         # let use a reccursive function that look for a rectangle with at least one ship
#         # for that we will divide the ship by four and then make 10 calls by ships.
#         # the rectangle that contain the ship will be the one we use for the next call 
#         # then we will divide that rectangle into 4 others rectangles. 
#         # to create the 4 rectangle we have to create 8 points for those 4 rectangle then call the hasShips method 10 times for each rectangle
#         
#
#         def func(self,top:Point,bott:Point)->int:
#             # if top < bott we have have to stop the search
#             if top.x < bott.x or bott.y > top.y:
#                 return 0
#             # check if the top is the same as the bottom
#             if top.x == bott.x and top.y == bott.y:
#                 # check if the rectangle has a ship
#                     return int(sea.hasShips(top,bott))
#             else:
#                 if not sea.hasShips(top,bott):
#                     return 0
#             # Now i have to create the different Point
#                 mx = (top.x + bott.x) // 2 
#                 my = (top.y + bott.y) // 2
#             # top rect
#                 a = func(top,Point(mx+1,my+1))
#             # left rect
#                 b = func(Point(top.x,my),Point(bott.x,my))
#             
#             # bott rect
#                 c = func(Point(mx,my),bott)
#
#             # righ rect 
#                 d = func(Point(top.x,my),Point(mx+1,bott.y))
#
#                 return a + b + c + d
#
#         return func(topRight,bottomLeft)
#     
    
# candy crush


# class Solution:
#     def candyCrush(self,board: List[List[int]])->List[List[int]]:
#         
#         # you have a m * n board matrix where baord[i][j] represent the value of board at position(i,j)
#         # Now they want you to restore the board to it stable state.
#         # rules: if they are three or more of the same type are adjacent vertically or horizontally 
#         # crush them  all the same time.
#
#         # initialize a boolean value which represent the state of the game
#         done = True
#
#
#         # first step---> tag all the adjacent candies horizontally
#         # run a double loop and switch all the groups of candies that are suitable for the rules to -1
#         for r in range(len(board)):
#             for c in range(len(board[r])-2):
#                 a = abs(board[r][c])
#                 b = abs(board[r][c+1])
#                 d = abs(board[r][c+2])
#                 if a == b and b == c and a != 0:
#                     board[r][c] = -a
#                     board[r][c+1] = -b
#                     board[r][c +2] = -d
#                     done = False
#
#         # second step --> tag all the adjacent candies vertically
#         # run a double a loop as well and switch all the grougps of candies suitable for the rules to -1 
#         # 
#
#         for c in range(len(board[0])):
#             for r in range(len(board)-2):
#                 a = abs(board[r][c])
#                 b = abs(board[r+1][c])
#                 d = abs(board[r+2][c])
#                 if a == b and b == c and a != 0:
#                     board[r][c] = -a
#                     board[r-1][c] = -b
#                     board[r-2][c] = -d
#                     done = False
#
#          
#         # then last crush them.
#         # only if not done meaning if either of the transformation occur done will be false otherwise it will be true
#         # only crush if done i false
#         if not done:
#             for c in range(len(board[0])):
#                 # the last index of the colunms
#                 idx = len(board)-1
#                 for r in range(len(board)-1,-1,-1):
#                     if board[r][c] > 0:
#                         board[idx][c] = board[r][c]
#                         idx -= 1
#                 # Now delete all the negative number to zero 
#                 for r in range(idx,-1,-1):
#                     board[r][c] = 0
#
#         return board if done else self.candyCrush(board)
#

# This problem solve the two cities travel cost.
#
# class Solution:
#     def twoCityScheduleCost(self,costs:List[List[int]])->int:
#         # to solve this problem with have to compute the difference between the two position
#         # then sort the the difference. 
#         # Since we have to share all the travel within all the user.
#         # we'll divide the list of diff by two and take half for the first part of the users
#         # then take the second part 
#         result = 0
#         diff = []
#         # run a loop and store the difference  of cost and the actual costs and the 
#         for a,b in costs:
#             diff.append([b-a,a,b])
#         # Now sort the diff, meaning we we'll choose the second cost for the first half of users
#         for i in range(len(diff)):
#             if i < len(diff)//2:
#                 result += diff[i][2]
#             else:
#                 result += diff[i][1]
#         return  result
#

# Invalid_transactions.
# class Solution:
#     def invalidTransactions(self,transactions:List[str])->List[str]:
#         # create a set to save all the index of the invalid transactions
#         invalid_trans = set()
#         # create default collections list
#         customers = defaultdict(list)
#
#         # run a loop to extract the names,amount , time for each transaction.
#         for index, trans in enumerate(transactions):
#             name,time,price,city = trans.split(" ")
#
#             # check if the price is over the bound
#             if int(price) > 1000:
#                 invalid_trans.add(index)
#             if not name in customers:
#                 customers[name].append((time,price,city))
#                 continue
#             # Now run another loop over the list of names and check if any transaction 
#             # has happened in less than the time. or just that the city aren the same.
#             for tx in customers[name]:
#                 if(city != tx[2] and abs(int(time)-tx[0])) < 60:
#                     invalid_trans.add(index)
#                     invalid_trans.add(tx[-1])
#             customers[name].append((time,price,city))
#
#         return [transactions[idx] for idx in invalid_trans]
#


#
# class Solution:
#     def removeDuplicates(self,s:str,k:int)->str:
#         # create a stack that takes [count,ch]
#         # run a loop over the string
#         # check if the present char is in the stack
#         # then increment the count
#         # else add a new pair to the stack
#         # Now check if the count of that char is equal to k
#         # pop the pair out the stack 
#         # then initiate the the result string 
#         # run a loop over the pairs in the stack
#         # add the to the intial result string the count * the char
#         # return the result string
#
#          

#
# class Solution:
#     # The give you a matrix of numbers '1' represent the a piece of land and the '0' represent earth
#     # Now the want you to find all the connected piece of lands that gives you what is called an island
#     # If there are more than one island, return them all
#     def numsOfIslands(self,grid:List[List[str]])->int:
#         # first we need a set to keep all the case visited
#         # then we'll write a reccursive function that will take
#         # two input a row and a colunm
#         # in the function run a loop to first find a 1 then call the function 
#         # 4 more times with input changing according 
#         visited = set()
#         def func(r,c):
#             if r <= 0 or c <= 0 or r > len(grid) or c > len(grid[0]) or (r,c) in visited:
#                 return 
#             if grid[r][c] == '0':
#                 return 
#             visited.add((r,c))
#             func(r,c+1)
#             func(r+1,c)
#             func(r-1,c)
#             func(r,c-1) 
#         # Now run a loop to find the '1'
#         result = 0
#         for r in range(len(grid)):
#             for c in range(len(grid[0])):
#                 if grid[r][c] == '1' and (r,c) not in visited:
#                     result += 1
#                     func(r,c)
#
#         return result
#

#
# class Solution:
#     def minMeetingRooms(self,interval:List[List[int]])->int:
#         # you are given a number of intervall meetings as a list of pair [a,b]
#         # you need to find how many rooms will be needed to fit all the meetings
#         # Now we will use a list to store all the starting and ending time
#         # if it's a starting we adding one room, otherwise we removing one room
#         # and at any point of time we should be keeping the track of the highest count of the rooms 
#         rooms = []
#
#         for s,e in interval:
#             rooms.append((s,1))
#             rooms.append((e,-1))
#         # Now we have the all the rooms we should sort them 
#         rooms.sort()
#         count = 0
#         max_count = 0
#
#         for _,d in rooms:
#             count += d
#             max_count = max(max_count,count)
#         return max_count
#
#

#
# class Solution:
#     def allPath(self,graph:List[List[int]])->List[List[int]]:
#         # So the idea is to find a path from one node to another one
#         # we'll use the def method.
#         # starting from the node_index 0 and an empty list
#         # if the node_index is equal to the length of the acyclic graph. return the result.appended(path,[u]) 
#         result = []
#         def dfs(path,index):
#             if index == len(graph)-1:
#                 return result.append(path + [index])
#             else:
#                 for v in graph[index]:
#                     dfs(path + [index],v)
#         
#         dfs(0,[])
#         return result
#
#
# class Solution:
#     #The is, you have a stream of input string that are paired with a idKey
#     # and we want to insert them into a container and return them 
#     # by order of the idKey. 
#
#     def __init__(self,n:int):
#         self.result = [] * (n + 1)
#         self.ptr = 1
#
#     def inputFunc(self,idKey:int,value:str):
#         self.result[idKey] = value
#         
#         rs = []
#         if idKey == self.ptr:
#             while self.result[self.ptr] and self.ptr < len(self.result):
#                 rs.append(self.result[self.ptr])
#                 self.ptr += 1
#         return rs

####### LRU Cache

class Solution:
    def __init(self,capacity:int):
        self.capacity = capacity
        self.data = {}
        self.stack = []


### function get that takes an input as an integer and return the value of the key if the keys exist otherwise return -1
    def get(self,key:int)->int:
        if not (key in self.data):
            return  -1

        return self.data[key]


### function put that takes an int as a key and int as value
# update the key-value paire if it exist otherwise add the key-value pair
# tot the cache. if the numbers of keys exceeds the capacity, evict the least recently used
# the function get and put must run on the O(1) meaning constant time complexity

    def put(self,key:int,value:int)->None:























       




























