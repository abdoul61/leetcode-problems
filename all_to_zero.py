# The Time complexity of this algorithm is (n) where n is the number of the nodes. and the space complexity is 0(n) 
# because we will need to save all the node in a dictionary
from typing import List
from collections import defaultdict
import time
class Solutions:
    def __init__(self,count:List):
        self.count = count
    #create a graph to map the derictions from parent to child
    graph = defaultdict(dict)
    visited =  set()
    def minReplacement(self,n:int,connections:List[List[int]]) -> int:
        # run a loop and map parent to child;if parent to child save 1 otherwise save 0
        for u,v in connections:
            self.graph[u][v] = 1
            self.graph[v][u] = 0

        # run a depth first search algorithm to retrieve all the couple and add the values that need to be replace.
        self.dfs(0,self.count)

        return self.count[0]
    def dfs(self,root:int,count:List) -> None:
        self.visited.add(root)
        for parent,val in self.graph[root].items():
            # check if the parent has been visited already
            if parent not in self.visited:
                # check if the the value save in 1 or 0
                if val == 1:
                    # increase the count
                    count[0] += 1
                # since the parent is not visited yet we should run recursively the dfs in the parent as well
                self.dfs(parent,count)
        


        
data = [[0,1],[1,3],[2,3],[4,0],[4,5]]
data2 = [[1,0],[1,2],[3,2],[3,4]]
#print(Solutions([0]).minReplacement(5,data))
#time.sleep(4)
print(Solutions([0]).minReplacement(4,data2))
