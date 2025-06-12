class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Approach: Sort candidates arr so distinct branches can't have
        # duplicate elements in them
        # Recursive DFS on decision tree
        # Time-Complexity: O(n * 2^n)
        # Space-Complexity: O(n)
        # n is len(candidates)
        
        res = []
        candidates.sort()

        def dfs(i, currArr, total):
            if total == target:
                res.append(currArr.copy())
                return
            if i >= len(candidates) or total > target:
                return
            
            # take element
            currArr.append(candidates[i])
            dfs(i + 1, currArr, total + candidates[i])
            currArr.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            # don't take element
            dfs(i + 1, currArr, total)

        dfs(0, [], 0)
        return res