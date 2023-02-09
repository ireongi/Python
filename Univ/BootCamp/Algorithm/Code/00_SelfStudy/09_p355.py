class Graph():
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

def print_graph(g):
    print('')