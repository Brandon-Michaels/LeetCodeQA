class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Approach:
        # Order does matter, no need to remove duplicates
        # Recursive calls on permute, recurse to base-case
        # then return permutations up the stack, adding in new 
        # number in between current permutations each call up the stack
        # Time-Complexity: O(n!)
        # Space-Complexity: O(n!)

        res = []

        # base-case
        if len(nums) == 0:
            return [[]]

        permutations = self.permute(nums[1:])

        for p in permutations:
            # insert in all locations (including end)
            for i in range(0, len(p) + 1):
                perm_copy = p.copy()
                perm_copy.insert(i, nums[0])
                res.append(perm_copy)
    
        return res
