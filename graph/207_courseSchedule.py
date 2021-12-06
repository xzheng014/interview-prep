class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        topological_sorted = []

        indegree = [0] * numCourses

        for prereq in prerequisites:
            indegree[prereq[0]] += 1

        queue = deque()

        for i in range(0, numCourses):
            if indegree[i] == 0:
                topological_sorted.append(i)
                queue.append(i)

        while queue:
            course = queue.popleft()
            for prereq in prerequisites:
                if prereq[1] == course:
                    indegree[prereq[0]] -= 1
                    if indegree[prereq[0]] == 0:
                        topological_sorted.append(prereq[0])
                        queue.append(prereq[0])

        return len(topological_sorted) == numCourses
