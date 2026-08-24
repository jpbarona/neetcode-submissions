class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(A,B,i,j):
            if j-i<0:
                return
            if j-i==1:
                B[i] = A[i]
                return
            
            k = (i+j)//2

            mergeSort(B,A,i,k)
            mergeSort(B,A,k,j)

            l,r = i,k
            for p in range(i,j):
                if l<k and (r==j or A[l]<=A[r]):
                    B[p] = A[l]
                    l+=1
                else:
                    B[p] = A[r]
                    r+=1
        
        B = nums.copy()
        mergeSort(nums,B,0,len(nums))
        return B

        