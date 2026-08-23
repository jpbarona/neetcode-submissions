class Solution:
    def trap(self, height: List[int]) -> int:
        out = 0
        if len(height) <= 2:
            return 0

        positiveNum = sum(x>0 for x in height)
        if positiveNum < 2:
            return 0
        
        while positiveNum >= 2:
            #While currentHeights is stil positive
            #Remove leading 0s
            zeroIndices = set()
            for i in range(len(height)):
                if height[i] == 0:
                    zeroIndices.add(i)

            #Remove left leading 0s
            if 0 in  zeroIndices:
                leftZero = 0
                for i in range(len(height)-1):
                    if i+1 in zeroIndices:
                        leftZero = i+1
                    else:
                        break

                height = height[leftZero+1:]

            zeroIndices = set()
            for i in range(len(height)):
                if height[i] == 0:
                    zeroIndices.add(i)

            #Remove right zeros
            if len(height)-1 in zeroIndices:
                rightZero = len(height)-1
                for i in range(len(height)-1, 1, -1):
                    if i-1 in zeroIndices:
                        rightZero = i-1
                    else:
                        break

                height = height[:rightZero]
            
            #For all 0 entries in new invariant list increase out by 1
            #Reduce all the heights by one
            #Add that to the running tally
            for i in range(len(height)):
                if height[i] == 0:
                    out += 1

                height[i] = max(height[i]-1, 0)

            

            positiveNum = sum(x>0 for x in height)

        return out

            
            
        


        