class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # target -nums[k]
        # sort nums increasing order
        # two ptr approach: if left + right is too small,
        # increment left, else decrement right
        # if match, add i,j,k to solution set, no duplicates
        # Time-Complexity: O(n^2)
        # Space-Complexity: O(1)

        res = set()
        nums.sort()

        for k in range(0, len(nums)):
            i = k + 1
            j = len(nums) - 1
            while (i < j):
                if (nums[i] + nums[j] == (-nums[k])):
                    curr_tuple = tuple(sorted([nums[i], nums[j], nums[k]]))
                    if (curr_tuple not in res):
                        res.add(curr_tuple)
                    i += 1
                    j -= 1
                elif (nums[i] + nums[j] < (-nums[k])):
                    i += 1
                else:
                    j -= 1

        return [list(t) for t in res]