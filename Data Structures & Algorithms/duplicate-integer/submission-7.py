class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniqueItems: set = set()
        for x in nums:
            if x in uniqueItems:
                return True
            uniqueItems.add(x)
        
        return False