class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #n^2 + n 
        sums = defaultdict(list)
        idxs = defaultdict(list)
        for i in range(len(nums)):
            f = nums[i]
            for j in range(len(nums)):
                b = nums[j]
                #x=-f-b
                if i != j:
                    sums[-f-b].append((f,b))
                    idxs[-f-b].append((i,j))

        out = []
        added = defaultdict(bool)

        for k in range(len(nums)):
            num = nums[k]
            if sums.get(num, None) is not None:
                for nMatch in range(len(sums[num])):
                    f,b = sums[num][nMatch]
                    i,j = idxs[num][nMatch]

                    if k in (i,j):
                        continue

                    result = sorted([f,num,b])

                    if not added[tuple(result)]:
                        out.append(result)
                        added[tuple(result)] = True
        
        return out


                