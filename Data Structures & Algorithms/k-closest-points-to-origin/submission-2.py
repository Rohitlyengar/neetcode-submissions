class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            dist = math.sqrt((x ** 2) + (y ** 2))
            heap.append([dist, x, y])

        heapq.heapify(heap)

        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1:3])
        
        return res
