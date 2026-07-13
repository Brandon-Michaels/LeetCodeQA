import heapq

class MedianFinder:

    def __init__(self):
        self.lower_half = []
        self.upper_half = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lower_half, -num)

        if self.upper_half and -self.lower_half[0] > self.upper_half[0]:
            largest_in_lower = -heapq.heappop(self.lower_half)
            heapq.heappush(self.upper_half, largest_in_lower)

        if len(self.lower_half) > len(self.upper_half) + 1:
            largest_in_lower = -heapq.heappop(self.lower_half)
            heapq.heappush(self.upper_half, largest_in_lower)
        elif len(self.upper_half) > len(self.lower_half):
            smallest_in_upper = heapq.heappop(self.upper_half)
            heapq.heappush(self.lower_half, -smallest_in_upper)

    def findMedian(self) -> float:
        if len(self.lower_half) > len(self.upper_half):
            return float(-self.lower_half[0])
        
        largest_in_lower = -self.lower_half[0]
        smallest_in_upper = self.upper_half[0]
        return (largest_in_lower + smallest_in_upper) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()