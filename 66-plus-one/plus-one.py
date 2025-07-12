class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Approach
        # Traverse through the digits list
        # add overflow
        # if one's digit is less than 9, then just return that number
        # if last digit happens to be 9, add one to next column
        # repeat for all entries in List
        # Time-Complexity: O(n), where n is len(digits)
        # Space-Complexity: O(1), excluding returning output array

        n = len(digits)
        output = [0] * (n + 1)
        carry = 1
        
        for i in range(n - 1, -1, -1):
            # add 1 to curr digit, if overflow carry
            
            total = carry + digits[i]
            output[i + 1] = total % 10
            carry = total // 10
            
        if carry == 1:
            output[0] = 1
            return output
        else:
            return output[1:]
