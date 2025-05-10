class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Intuition: 
        # if you traverse and find number => push to stack
        # if you find operator, pop prev 2 elements
        # perform operation and store result back on stack
        # Time-Complexity: O(n), n is size of tokens list
        # Space-Complexity: O(n), stack size (roughly n)

        stack = []

        for i in range(0, len(tokens)):
            if (tokens[i] == "+"):
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1 + num2)
            elif (tokens[i] == "-"):
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 - num1)
            elif (tokens[i] == "*"):
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1 * num2)
            elif (tokens[i] == "/"):
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(int(float(num2 / num1)))
            else:
                curr_num = int(tokens[i])
                stack.append(curr_num)
                
        return int(stack.pop())
