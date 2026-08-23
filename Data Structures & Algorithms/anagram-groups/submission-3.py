class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap: dict[str, list[int]] = {}
        for i in range(len(strs)):
            x = strs[i]
            letters = "".join(sorted(x))
            hashmap[letters] = [i] + hashmap.get(letters, [])

        result = [[strs[i] for i in idx] for idx in hashmap.values()]
        return result