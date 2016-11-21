from Graph import *

class DirectedGraph(Graph):

    def __init__(self, num_nodes):
        Graph.__init__(self, num_nodes)

    def connect(self, index1, index2):
        self.adjacency_dict[index1].add(index2)


    def has_cycle(self):
        #To do:
        pass




