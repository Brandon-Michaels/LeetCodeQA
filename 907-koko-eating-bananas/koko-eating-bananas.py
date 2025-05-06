class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Approach
        # binary search on min k array from [0, max(piles[i])]
        # Pick a value in k array
        # Then iterate over piles, if it's doable, decrease right ptr and try
        # new value, else if not doable increase left ptr
        # repeat until left and right converge at same value in k array
        # Time-Complexity: O(nlogn)
        # Space-Complexity: O(1)

        max_val = 0

        # compute max in piles
        for num in piles:
            max_val = max(num, max_val)
        
        left = 1
        right = max_val

        while (left < right):
            k = (left + right) // 2
            hours = 0

            # compute time it takes to eat all bananas
            for num in piles:
                if (num < k):
                    hours += 1
                elif (num % k == 0):
                    hours += (num / k)
                else:
                    hours += ((num // k) + 1)
            
            # try minimizing further
            if (hours <= h):
                right = k
            # if not doable, try larger k
            else:
                left = k + 1

        return left