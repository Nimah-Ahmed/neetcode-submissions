"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        visited = set()
        created_but_not_completed = {}
        def getClone(clone_node, og_node):
            # base case
            # recursive case
            to_recurse = []
            for og_neighbor in og_node.neighbors:
                if og_neighbor in created_but_not_completed:
                    created_clone_neighbor = created_but_not_completed[og_neighbor]
                    clone_node.neighbors.append(created_clone_neighbor)
                    created_clone_neighbor.neighbors.append(clone_node)
                elif og_neighbor not in visited:
                    clone_neighbor = Node(og_neighbor.val, [clone_node])
                    clone_node.neighbors.append(clone_neighbor)
                    created_but_not_completed[og_neighbor] = clone_neighbor
                    to_recurse.append((clone_neighbor, og_neighbor))
            visited.add(og_node)
            if og_node in created_but_not_completed:
                del created_but_not_completed[og_node]
            for cn, on in to_recurse:
                getClone(cn, on)

        if node == None:
            return node
        clone_node = Node(node.val, None)
        getClone(clone_node, node)
        return clone_node
                    
