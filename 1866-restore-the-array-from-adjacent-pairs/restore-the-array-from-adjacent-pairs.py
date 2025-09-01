# adjacentPairs[i] = [ui, vi] indicates that the elements ui and vi are adjacent in nums.
# Restore the array from Adjacent Pairs

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        # Build an undirected adjacency list: val -> list of its neighbors
        adj = defaultdict(list)                       # maps element to its neighbors
        for a, b in adjacentPairs:                    # process each given adjacent pair
            adj[a].append(b)                          # add both directions since adjacency is mutual
            adj[b].append(a)

        # Find an endpoint, the element with degree 1, which must be one of the array ends
        start = None
        for x, nbrs in adj.items():                   # scan all nodes once
            if len(nbrs) == 1:                        # endpoint has exactly one neighbor
                start = x
                break

        # Initialize result with the start, then walk the path using neighbor info
        n = len(adj)                                  # number of distinct elements equals array length
        res = [0] * n                                 # preallocate result for O(1) appends by index
        res[0] = start                                # first element is an endpoint
        if n == 1:                                    # guard, though by problem, n >= 2
            return res

        # Second element is the only neighbor of the start
        res[1] = adj[start][0]                        # degree 1 guarantees exactly one neighbor

        # For each next position, choose the neighbor that's not the previous element
        for i in range(2, n):                         # fill positions 2..n-1
            prev = res[i - 2]                         # previous previous element
            curr = res[i - 1]                         # current element
            a, b = adj[curr] if len(adj[curr]) == 2 else (adj[curr][0], None)
            # If curr is an interior node it has two neighbors, pick the one not equal to prev.
            # If curr is an endpoint, it has one neighbor and b is None, loop ends next step.
            res[i] = a if a != prev else b            # choose the unused neighbor

        return res