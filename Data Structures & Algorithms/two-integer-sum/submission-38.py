class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0,1]

        #sort (nlog(n))
        A = [(i, nums[i]) for i in range(len(nums))]

        A.sort(key=lambda x: x[1])

        i = 0
        j = len(nums)-1

        while i < j:
            addition = A[i][1] + A[j][1]
            if addition == target:
                return [
                    min(A[i][0], A[j][0]),
                    max(A[i][0], A[j][0])
                    ]
            
            #If addition is less, move i up
            #If it is more, move j down
            if addition < target:
                i += 1
            if addition > target:
                j -=1

        return []


        