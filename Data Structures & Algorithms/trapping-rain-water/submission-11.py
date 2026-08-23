class Solution:
    def trap(self, height: List[int]) -> int:
        out = 0
        if len(height) <= 2:
            return 0

        positiveNum = sum(x>0 for x in height)
        if positiveNum < 2:
            return 0
        
        while positiveNum >= 2:
            #Remove leading 0s
            left = 0
            while left<len(height) and (height[left] == 0):
                left+=1

            right = len(height)-1  
            while right>0 and (height[right] == 0):   
                right -=1

            height = height[left:right+1]    
            
            #For all 0 entries in new invariant list increase out by 1
            #Reduce all the heights by one
            #Add that to the running tally
            for i in range(len(height)):
                if height[i] == 0:
                    out += 1

                height[i] = max(height[i]-1, 0)

            

            positiveNum = sum(x>0 for x in height)

        return out

            
            
        


        