class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Group by letters
        #Return the groups
        #In any order => Hashmap.
        #Hashmap has O(1) lookup, so we can sort and store in Hashmap

        hashmap: dict[str, list[int]] = {}
        for i in range(len(strs)):
            x = strs[i]
            letters = "".join(sorted(x))
            hashmap[letters] = [i] + hashmap.get(letters, [])

        #[[0,2], [1]]
        result = [[strs[i] for i in idx] for idx in hashmap.values()]
        return result