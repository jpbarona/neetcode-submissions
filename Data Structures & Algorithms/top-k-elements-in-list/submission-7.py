class Solution: 
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        for n in nums:
            hashmap[n] += 1

        freqBuckets = [[] for _ in range(len(nums) + 1)]

        for x, freq in hashmap.items():
            freqBuckets[freq].append(x)
        
        ptr = len(freqBuckets) - 1
        
        result = []
        while len(result) < k:
            currentFreq = freqBuckets[ptr]
            if len(currentFreq) > 0:
                result.extend(currentFreq)
            ptr -= 1

        return result