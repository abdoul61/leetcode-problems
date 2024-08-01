# This is the Least Recent Used 

# Here we'll use linkedList as Node
class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.next = self.prev= None

#if this program doe not work i could still make a use or other thing that cou
class LRUCache:
    def __init__(self,capacity:int):
    # This is the max capacity the cache can take
        self.cap = capacity
    # This is the cache. Here we will use a hashmap
        self.cache = {} # it will map a key to a Node
    # Here we need two dummy Node left and right. left will represent the least recently used and right will represent the most recent used
    # Any new Node will be inserted in between these two Nodes
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next , self.right.prev = self.right, self.left

# This is a helper function to help us remove the a Node 
    def remove(self,node):
        prev,nxt = node.prev,node.next
        prev.next,nxt.prev = nxt,prev
        

# This is a helper function to help use add Node 
    def insert(self,node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.left = nxt, prev


# This function takes an input key and return a value
# if the key exit in the cache, then return the value
# otherwise return -1
    def get(self,key:int)->int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

#This function is the put function that takes two inputs a key and value.
# add the key to the value inside the map:
# --> if the key is already in the cache update the value of the key
# --> if the pair [key,val] not in the cache, save the pair
# --> if the capacity of the cache is exosted, then remove the least recently used [key,val] from the cache

    def put(self,val,key)->None:
        if key in self.cache:
            # remove the Node from the list
            self.remove(self.cache[key])
        # Now add it with the new value
        self.cache[key] = Node(key,val)
        # Then insert it in the list
        self.insert(self.cache[key])

        # Now if the capacity of the hashmap has exced 
        if len(self.cache) > self.cap:
            # remove from the list and remove from the hashmap
            lru = self.left.next 
            self.remove(lru)
            del self.cache[lru.key]
        








