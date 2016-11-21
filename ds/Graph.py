from collections import deque


class Graph:
    def __init__(self, num_nodes):
        self.nodes = range(num_nodes)
        self.adjacency_dict = {node: set() for node in self.nodes}
        self.visited = [False] * num_nodes
        self.distance_count = [0] * num_nodes

    def check_visited(self, node):
        return self.visited[node]

    def update_visited(self, node):
        self.visited[node] = True

    def connect(self, index1, index2):
        self.adjacency_dict[index1].add(index2)
        self.adjacency_dict[index2].add(index1)

    def reset(self):
        self.visited = [False for i in self.visited]
        self.distance_count = [-1 for i in self.distance_count]

    def get_bfs(self, node):
        self.update_visited(node)
        queue = deque([node])
        self.distance_count[node] = 0
        while len(queue) > 0:
            element = queue.popleft()
            # Update distances of neighbours
            for neighbour in self.adjacency_dict[element]:
                if self.check_visited(neighbour) is False:
                    queue.append(neighbour)
                    self.update_visited(neighbour)
                    self.distance_count[neighbour] = self.distance_count[element] + 1
        self.distance_count = [x if x > 0 else -1 for x in self.distance_count]

    def get_dfs(self,node):
        self.update_visited(node)
        connected_nodes=[]
        stack = [node]
        while len(stack) > 0 :
            element = stack.pop()
            for neighbour in self.adjacency_dict[element]:
                if self.check_visited(neighbour) is False:
                    self.update_visited(neighbour)
                    stack.append(neighbour)
                    connected_nodes.append(neighbour)
        return connected_nodes

    def find_all_distances(self, starting_index):
        self.reset()
        self.get_bfs(starting_index)
        updated_distance_count = self.distance_count[0:starting_index] + self.distance_count[starting_index + 1:]
        print " ".join([str(distance) for distance in updated_distance_count])

