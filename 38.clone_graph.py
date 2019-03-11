# Clone an undirected graph. Each node in the graph contains a label and a list
# of its neighbors.
#
# OJ's undirected graph serialization:
# Nodes are labeled uniquely.
#
# We use # as a separator for each node, and , as a separator for node label and
# each neighbor of the node.

# As an example, consider the serialized graph {0,1,2#1,2#2,2}.
#
# The graph has a total of three nodes, and therefore contains three parts as
# separated by #.
#
# First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
# Second node is labeled as 1. Connect node 1 to node 2.
# Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a
# self-cycle.
# Visually, the graph looks like the following:
#
#        1
#       / \
#      /   \
#     0 --- 2
#          / \
#          \_/
#
# Time:  O(n)
# Space: O(n)
#

from model import UndirectedGraphNode


class Solution:
    def __init__(self):
        self.cloned = dict()
        self.queue = list()

    def clone_graph(self, node):
        if node is None:
            return None

        self.clone(node)
        while self.queue:
            current = self.queue.pop()
            for neighbor in current.neighbors:
                if neighbor not in self.cloned:
                    self.clone(neighbor)
                self.cloned[current].neighbors.append(self.cloned[neighbor])
        return self.cloned[node]

    def clone(self, node):
        cloned_node = UndirectedGraphNode(node.label)
        self.cloned[node] = cloned_node
        self.queue.append(node)


if __name__ == '__main__':
    n1 = UndirectedGraphNode(1)
    n0 = UndirectedGraphNode(0)
    n2 = UndirectedGraphNode(2)
    n1.neighbors = [n0, n2]
    n0.neighbors = [n1, n2]
    n2.neighbors = [n0, n1, n2]
    s = Solution()
    s.clone_graph(n1)
    for n in s.cloned:
        print(n)
