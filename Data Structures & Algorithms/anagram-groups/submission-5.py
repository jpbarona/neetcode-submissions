class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for i in range(len(strs)):
            x = strs[i]

            chars = [0] * 26
            for c in x:
                chars[ord(c.lower()) - ord("a")] += 1
            
            key = tuple(chars)
            hashmap[key].append(x)

        return list(hashmap.values())

