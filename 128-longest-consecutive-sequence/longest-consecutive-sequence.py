class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Add each element in nums to set
        # If nums[i] - 1 DNE in set, then nums[i] == start of seq
        # then track max len of consecutive seq by seeing if nums[i + 1] + ...
        # return longest consecutive sequence
        # Time-Complexity: O(n), where n is length of nums list
        # Space-Complexity: O(n), where n is length of nums list

        longestSeq = set(nums)
        maxLength = 0

        for num in longestSeq:
            # start of seq
            if (num - 1) not in longestSeq:
                currLength = 1
                while (num + currLength) in longestSeq:
                    currLength += 1
                maxLength = max(maxLength, currLength)
        
        return maxLength