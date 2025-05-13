class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Intuition:
        # Sort array based on position
        # use stack to add (position, speed) cars 
        # if car catches up to another car, remove it from stack
        # else keep it, return len(stack), iterate right to left
        # Time-Complexity: O(nlogn)
        # Space-Complexity: O(n)

        mergedArr = [0] * len(position)
        for i in range(0, len(position)):
            mergedArr[i] = ((position[i]), (speed[i]))
        
        sortedPos = sorted(mergedArr, key=lambda x: x[0])
        stack = []
        arrivalTime = 0

        for i in range(len(sortedPos) - 1, -1, -1):
            currPos = (target - sortedPos[i][0])
            currSpeed = sortedPos[i][1]
            arrivalTime = float(currPos / currSpeed)
            stack.append(arrivalTime)

            if (len(stack) > 1 and arrivalTime <= stack[-2]):
                stack.pop()

        return len(stack)