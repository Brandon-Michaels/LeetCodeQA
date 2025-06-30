class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Approach
        # DFS from 0 to highest course num
        # make sure that it isn't a prereq for anything
        # Time-Complexity: O(V + E), where V is nodes, E is prereqs
        # Space-Complexity: O(V + E)

        # map course to empty list initially
        adjacencyMap = {i:[] for i in range(numCourses)}
        visited = set()

        # add prereqs
        for course, prereq in prerequisites:
            # course : [list of prereqs]
            adjacencyMap[course].append(prereq)

        def dfs(course):
            # base-cases
            if course in visited:
                return False
            if adjacencyMap[course] == []:
                return True
            
            visited.add(course)
            for prereq in (adjacencyMap[course]):
                if not dfs(prereq):
                    return False
            visited.remove(course)
            # time-saver, imm know course can be complete
            # don't DFS if we know we can alr complete it
            adjacencyMap[course] = []
            return True
        
        for i in range(0, numCourses):
            if not dfs(i):
                return False
        
        return True