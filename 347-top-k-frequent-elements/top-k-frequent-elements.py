class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Approach:
        # Keep frequencies of array in HashMap
        # Add frequencies to Heap
        # remove max from Heap
        # repeat k times

        # Dictionary/HashMap
        # Key: nums[i], value: count(nums[i])
        frequency_nums = {}
        output = []

        for i in range(len(nums)):
            frequency_nums[nums[i]] = 1 + frequency_nums.get(nums[i], 0)
        
        heap = []
        for num in frequency_nums.keys():
            heapq.heappush(heap, (-frequency_nums[num], num))
        
        for i in range(k):
            output.append(heapq.heappop(heap)[1])
        
        return output