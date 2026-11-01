class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            stone1 = heapq.heappop_max(stones)
            stone2 = heapq.heappop_max(stones)

            heapq.heappush_max(stones, abs(stone1 - stone2))
        return heapq.heappop_max(stones)
