class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        while low < high:
            mid = (low + high) // 2
            hours = 0
            for i in piles:
                hour = (i + mid - 1) // mid
                hours += hour

            if hours > h:
                low = mid + 1
            elif hours <= h:
                high = mid
        return low