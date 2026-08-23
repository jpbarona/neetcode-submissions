class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        #[2,3,5,7,9,11,13]
        #8


        while i < j:
            if numbers[i] + numbers[j] > target:
                j -= 1
            if numbers[i] + numbers[j] < target:
                i += 1
            
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]

        return []
            