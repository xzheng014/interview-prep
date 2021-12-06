class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        if not rooms or len(rooms) == 1: return True

        visited = []

        def dfs(i):
            if i < 0 or i >= len(rooms):
                return
            for key in rooms[i]:
                if key not in visited:
                    visited.append(key)
                    dfs(key)
            return

        visited = [0]
        dfs(0)

        return len(visited) == len(rooms)

