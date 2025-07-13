class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Approach
        # Use heap (python default min-heap) to store stone weights
        # then pop 2 largest, and if they are equal remove both from heap
        # else remove one and push back second stone onto heap
        # with value of (subtract smaller from larger)
        # repeat until 1 stone remaining or nothing left
        # Time-Complexity: O(n), where n is len(stones)
        # Space-Complexity: O(n), where n is len(stones) for heap space

        stone_heap = []

        for stone in stones:
            heapq.heappush(stone_heap, -1 * stone)
        
        # most negative will be largest in min-heap
        while (len(stone_heap) > 1):
            x = (-1 * heapq.heappop(stone_heap))
            y = (-1 * heapq.heappop(stone_heap))
            if x < y:
                heapq.heappush(stone_heap, -1 * (y - x))
            elif (y < x):
                heapq.heappush(stone_heap, -1 * (x - y))

        return ((-1) * heapq.heappop(stone_heap)) if stone_heap else 0