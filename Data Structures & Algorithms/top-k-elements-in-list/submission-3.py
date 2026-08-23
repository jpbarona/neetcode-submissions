class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        for n in nums:
            hashmap[n] += 1
        
        kvZip = zip(hashmap.keys(), hashmap.values())
        keyValues = sorted(list(kvZip), key=lambda x: x[1], reverse=True)
        sortedValues = [keyValues[i][0] for i in range(k)]

        return sortedValues
        