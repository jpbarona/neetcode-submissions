from _heapq import heappush
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        def getCapacity(l: int, r: int) -> int:
            minHeight = min(heights[l], heights[r])
            return minHeight * abs(l-r)

        l, r = 0, len(heights)-1

        maxCapacity = 0
        while l<r:
            currentCapacity = getCapacity(l,r)

            leftH = heights[l]
            rightH = heights[r]
            if leftH  > rightH:
                r -= 1
            elif leftH < rightH:
                l += 1
            elif leftH == rightH:
                l +=1

            maxCapacity = max(maxCapacity, currentCapacity)

        return maxCapacity



