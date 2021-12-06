"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node: return node

        self.explored = {}

        queue = deque([node])

        self.explored[node] = Node(node.val, [])

        while queue:
            temp = queue.popleft()
            for neighbor in temp.neighbors:
                if neighbor not in self.explored:
                    self.explored[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)
                self.explored[temp].neighbors.append(self.explored[neighbor])

        return self.explored[node]


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution(object):

    def __init__(self):
        self.explored = {}

    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node: return node

        if node in self.explored:
            return self.explored[node]

        clone_node = Node(node.val, [])
        self.explored[node] = clone_node

        for neighbor in node.neighbors:
            self.explored[node].neighbors.append(self.cloneGraph(neighbor))

        return clone_node
