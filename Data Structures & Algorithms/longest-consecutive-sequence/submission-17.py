class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        numsSorted = sorted(nums)

        longestSeq = 1
        currentSeq = 1

        for i in range(1, len(nums)):
            if numsSorted[i] == numsSorted[i-1] + 1:
                currentSeq += 1
            elif numsSorted[i] == numsSorted[i-1]:
                    continue
            else:
                longestSeq = max(currentSeq, longestSeq)
                currentSeq = 1
            
        longestSeq = max(currentSeq, longestSeq)

        return longestSeq


            
        

            
