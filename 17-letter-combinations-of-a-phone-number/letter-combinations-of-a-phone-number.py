class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Approach
        # create hashmap where digit : chars list
        # for each digit go through all subsequent digit(s) letters
        # recursive DFS
        # Time-Complexity: O(4^n), where n is number of digits
        # Space-Complexity: O(n)

        res = []
        digitsToChar = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            if i >= len(digits):
                return
            
            for c in digitsToChar[digits[i]]:
                backtrack(i + 1, curStr + c)
            
            
        if digits:
            backtrack(0, "")

        return res