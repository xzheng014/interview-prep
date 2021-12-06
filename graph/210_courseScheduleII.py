class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        topological_sorted = []

        indegrees = [0] * numCourses

        for prereq in prerequisites:
            indegrees[prereq[0]] += 1

        queue = deque()

        for course in range(0, numCourses):
            if indegrees[course] == 0:
                topological_sorted.append(course)
                queue.append(course)

        while queue:
            course = queue.popleft()
            for prereq in prerequisites:
                if prereq[1] == course:
                    indegrees[prereq[0]] -= 1
                    if indegrees[prereq[0]] == 0:
                        topological_sorted.append(prereq[0])
                        queue.append(prereq[0])

        if len(topological_sorted) == numCourses:
            return topological_sorted
        else:
            return []


