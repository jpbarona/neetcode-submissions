class Solution:
    def findLucky(self, arr: List[int]) -> int:
        out = -1
        count = {}
        for x in arr:
            count[x] = count.get(x,0)+1
        
        for key,value in zip(count.keys(), count.values()):
            if key == value and key>out:
                out=key
        

        return out


        