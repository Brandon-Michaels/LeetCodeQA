class Solution:
    def isHappy(self, n: int) -> bool:
        # Approach
        # add all nums to set for this calculation
        # while nums not repeated in set
        # keep going, if cycle set will detect it, then return false
        # Time-Complexity: O(n), where n is len(nums)
        # Space-Complexity: O(n), n is len(nums)

        visited = set()

        currSum = 0
        while (n != 0):
            currSum += ((n % 10) ** 2)
            n = (int)(n / 10)

        while (currSum != 1):
            if currSum in visited:
                return False
            visited.add(currSum)

            # repeat loop
            temp = currSum
            currSum = 0
            while (temp != 0):
                currSum += ((temp % 10) ** 2)
                temp = (int)(temp / 10)

        return True
        