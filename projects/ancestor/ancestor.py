from util import Stack, Queue

ea = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        # self.vertices[vertex_id] = set() #set of edges from this vert
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()


    def add_edge(self, v1, v2):
        # self.vertices[v1].add(v2)
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex does not exist in graph")

    def get_neighbors(self, vertex_id):
        print(self.vertices[vertex_id])
        return self.vertices[vertex_id]

    def bfs(self, starting_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breadth-first order.
        """
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        q = Queue()
        q.enqueue([starting_vertex])
		# Create a Set to store visited vertices
        visited = set()
		# While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first PATH
            path = q.dequeue()
            # Grab the last vertex from the PATH
            last = path[-1]
			# If that vertex has not been visited...
            if last not in visited:
                # CHECK IF IT'S THE TARGET
                # if last == destination_vertex:
                    # IF SO, RETURN PATH
                    # return path				  
				# Mark it as visited...
                visited.add(last)
				# Then add A PATH TO its neighbors to the back of the queue
                for neighbor in self.get_neighbors(last):
                    # COPY THE PATH
                    copy = list(path)
                    # APPEND THE NEIGHBOR TO THE BACK
                    copy.append(neighbor)
                    q.enqueue(copy)

#     10
#     /
#    1   2   4  11
#     \ /   / \ /
#      3   5   8
#       \ / \   \
#        6   7   9


def earliest_ancestor(ancestors, starting_node):
    g = Graph()

    # g.add_vertex(1)
    # g.add_vertex(2)
    # g.add_vertex(3)
    # g.add_vertex(4)
    # g.add_vertex(5)
    # g.add_vertex(6)
    # g.add_vertex(7)
    # g.add_vertex(8)
    # g.add_vertex(9)
    # g.add_vertex(10)
    # g.add_vertex(11)
    # g.add_edge(1, 3)
    # g.add_edge(2, 3)
    # g.add_edge(3, 6)
    # g.add_edge(5, 6)
    # g.add_edge(5, 7)
    # g.add_edge(4, 5)
    # g.add_edge(4, 8)
    # g.add_edge(8, 9)
    # g.add_edge(11, 8)
    # g.add_edge(10, 1)
# [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
# do a for loop to add the vertices and edges. 
    for x in ancestors:
        g.add_vertex(x[0])
        g.add_vertex(x[1])
        g.add_edge(x[1], x[0])

    q = Queue()
    q.enqueue([starting_node])
    tracker = []
    d = {}
    
    visited = set()

    while q.size() > 0:
        path = q.dequeue()
        last = path[-1]

        if last not in visited:
            visited.add(last)
            
            for neighbor in g.get_neighbors(last):
                copy = list(path)
                copy.append(neighbor)
                q.enqueue(copy)
                tracker.append(copy)
    longest = [-1]
    # ancestor = -1
    for paths in tracker:
        if len(paths) > len(longest):
            longest = paths
        if len(paths) == len(longest):
            if paths[-1] < longest[-1]:
                longest = paths
            
    return longest[-1]

print(earliest_ancestor(ea, 9))

#     10
#     /
#    1   2   4  11
#     \ /   / \ /
#      3   5   8
#       \ / \   \
#        6   7   9