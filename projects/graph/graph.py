"""
Simple graph implementation
""" 
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set() #set of edges from this vert

    def add_edge(self, v1, v2):
        # self.vertices[v1].add(v2)
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex does not exist in graph")

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def bft(self, starting_vertex_id):
        q = Queue()
        q.enqueue(starting_vertex_id)

        visited = set()

        while q.size() > 0:
            v = q.dequeue()

            if v not in visited:
                print(v)

                visited.add(v)

                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        # print(starting_vertex)
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        s.push(starting_vertex)

        visited = set()

        while s.size() > 0:
            v = s.pop()

            if v not in visited:
                print(v)

                visited.add(v)

                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)
        # if visited is None:
        #     visited = set()

        # visited.add(starting_vertex)

        # for child_vertex in self.vertices[starting_vertex]:
        #     if child_vertex not in visited:
        #         self.dft_recursive(child_vertex, visited)

    def dft_recursive(self, starting_vertex, visited=None):
        # print(starting_vertex)
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()

        visited.add(starting_vertex)

        print(starting_vertex)

        for neighbors in self.vertices[starting_vertex]:
            if neighbors not in visited:
                self.dft_recursive(neighbors, visited)

    def bfs(self, starting_vertex, destination_vertex):
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
                if last == destination_vertex:
                    # IF SO, RETURN PATH
                    return path				  
				# Mark it as visited...
                visited.add(last)
				# Then add A PATH TO its neighbors to the back of the queue
                for neighbor in self.get_neighbors(last):
                    # COPY THE PATH
                    copy = list(path)
                    # APPEND THE NEIGHBOR TO THE BACK
                    copy.append(neighbor)
                    q.enqueue(copy)			  


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        s.push([starting_vertex])
		# Create a Set to store visited vertices
        visited = set()
		# While the stack is not empty...
        while s.size() > 0:
            # Push the first PATH
            path = s.pop()
            # Grab the last vertex from the PATH
            last = path[-1]
			# If that vertex has not been visited...
            if last not in visited:
                # CHECK IF IT'S THE TARGET
                if last == destination_vertex:
                    # IF SO, RETURN PATH
                    return path				  
				# Mark it as visited...
                visited.add(last)
				# Then add A PATH TO its neighbors to the back of the stack
                for neighbor in self.get_neighbors(last):
                    # COPY THE PATH
                    copy = list(path)
                    # APPEND THE NEIGHBOR TO THE BACK
                    copy.append(neighbor)
                    s.push(copy)	

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        # print(starting_vertex)
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        
        if path is None:
            path = []

        visited.add(starting_vertex)

        path = path + [starting_vertex]
        
        if starting_vertex == destination_vertex:
            return path

        for neighbor in self.vertices[starting_vertex]:
            if neighbor not in visited:
                new_path = self.dfs_recursive(neighbor, destination_vertex, visited, path)

                if new_path:
                    return new_path

        return None

        
if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
