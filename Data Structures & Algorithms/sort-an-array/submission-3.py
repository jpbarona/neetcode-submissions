class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(A: list[int], B: list[int]) -> list[int]:
            out = [0] * (len(A)+len(B))
            i,j,k=0,0,0
            for k in range(len(out)):
                if i == len(A):
                    out[k] = B[j]
                    j+=1
                    continue
                
                if j == len(B):
                    out[k] = A[i]
                    i+=1
                    continue
                
                if A[i]<=B[j]:
                    out[k] = A[i]
                    i+=1
                elif B[j]<A[i]:
                    out[k]=B[j]
                    j+=1
            
            return out

        def mergeSort(x: list[int]) -> list[int]:
            if len(x)==1:
                return x
            mid = int(len(x)/2)
            A = mergeSort(x[:mid])
            B = mergeSort(x[mid:])
            return merge(A,B)
        
        return mergeSort(nums)

                
                
