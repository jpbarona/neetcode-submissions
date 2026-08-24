class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(src: list[int], dst: list[int], i: int, j: int) -> None:
            if j-i<=0:
                return
            if j-i==1:
                dst[i] = src[i]
                return
            
            k = (i+j)//2
            mergeSort(dst,src,i,k)
            mergeSort(dst,src,k,j)

            l,r = i,k
            for p in range(i,j):
                if l<k and (r>=j or src[l]<=src[r]):
                    dst[p] = src[l]
                    l+=1
                else:
                    dst[p] = src[r]
                    r+=1
            
        B = nums.copy()
        mergeSort(B, nums, 0, len(nums))
        return nums
