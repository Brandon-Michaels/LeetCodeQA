class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Intuition: add temps to stack, if current element is greater
        # then we can subtract diff of current element idx and top of stack
        # add this to respective idx in result
        # Time-Complexity: O(n), n is length of temperatures list
        # Space-Complexity: O(n), n is size of stack max(len(temp list))

        # pair (temp, index)
        stack = []
        res = [0] * len(temperatures)

        for i in range(0, len(temperatures)):
            while (len(stack) > 0 and stack[-1][0] < temperatures[i]):
                _, index = stack.pop()
                res[index] = i - index
            stack.append((temperatures[i], i))
        
        return res
        