class Solution:
    def isValid(self, s: str) -> bool:
        # Approach
        # push open characters on stack
        # when see closing character, pop character and ensure it matches open
        # if it doesn't return false, else true
        # Time-Complexity: O(n), where n is size of input string s
        # Space-Complexity: O(n), n is size of input string s

        stack = []

        for char in s:
            if (char == '[' or char == '{' or char == '('):
                stack.append(char)
            else:
                if (len(stack) > 0):
                    if (char == '}'):
                        if (stack[-1] == '{'):
                            stack.pop()
                        else:
                            return False
                    elif (char == ']'):
                        if (stack[-1] == '['):
                            stack.pop()
                        else:
                            return False
                    elif (char == ')'):
                        if (stack[-1] == '('):
                                stack.pop()
                        else:
                            return False
                else:
                    return False
        
        return len(stack) == 0