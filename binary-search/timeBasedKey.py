

from typing import List


class TimeMap:
    def __init__(self):
        self.store = {}

    def set(self,key:str,value:str,timestamp:int)->None:
        #set a key->pair value
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value,timestamp])
        print(self.store)


    def get(self,key:str,timestamp:int)->str:
        result = ""
        myList = self.store.get(key,[])
        l,r = 0,len(myList)-1
        while l <= r:
            mid = (l + r)//2
            if  timestamp >= myList[mid][-1]:
                result = myList[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return result




#Input
#["TimeMap", "set", "get", "get", "set", "get", "get"]
#[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
#Output
#[null, null, "bar", "bar", null, "bar2", "bar2"]
timeMap = TimeMap();
print(timeMap.set("foo", "bar", 1))  #// store the key "foo" and value "bar" along with timestamp = 1.
print(timeMap.get("foo", 1))         #// return "bar"
print(timeMap.get("foo", 3))         #// return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
print(timeMap.set("foo", "bar2", 4)) #// store the key "foo" and value "bar2" along with timestamp = 4.
print(timeMap.get("foo", 4))         #// return "bar2"
print(timeMap.get("foo", 5))       #// return "bar2"

