class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Approach:
        # Same approach as before
        # Recursive DFS on the pre-req tree
        # when you get to bottom of recursion, add that course to the res
        # so we know we can take that course first
        # Post-Order traversal
        # Build the pre-req tree using HashMap (course : list[pre-reqs])
        # Time-Complexity: O(V + E), v is courses, e is edges representing pre-reqs of that course
        # Space-Complexity: O(V + E)

        res = []
        # visited = course can be completed
        visited = set()

        # current courses we're seeing
        cycle = set()
        coursePreReqMap = {i : [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            coursePreReqMap[course].append(prereq)

        def dfs(course):
            if course in visited:
                return True
            if course in cycle:
                return False

            cycle.add(course)
            for c in coursePreReqMap[course]:
                if not dfs(c):
                    return False
            
            res.append(course)
            cycle.remove(course)
            visited.add(course)
            return True

        for i in range(0, numCourses):
            if not dfs(i):
                return []

        return res

