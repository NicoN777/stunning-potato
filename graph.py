from collections import defaultdict
from queue import PriorityQueue
import math


class Node:
    def __init__(self, data):
        self.data = data
        self.visited = False

    def __repr__(self):
        return f'Node({self.data})'

    def __lt__(self, other):
        return self.data < other.data

    def __eq__(self, other):
        return self.data == other.data

    def __hash__(self):
        return hash(repr(self))


class Edge:
    def __init__(self, v: Node, weight: int):
        self.v = v
        self.weight = weight

    def __repr__(self):
        return f'Edge({repr(self.v)}, {self.weight})'

    def __lt__(self, other):
        return self.weight < other.weight

    def __eq__(self, other):
        return self.weight == other.weight

    def __hash__(self):
        return hash(repr(self))


class Graph:
    def __init__(self, edges: list):
        self.edges = edges
        self.graph = defaultdict(list)
        for u, v, w in self.edges:
            self.graph[Node(u)]
            self.graph[Node(v)]

        for _ in self.edges:
            source, dest, weight = _
            source = Node(source)
            dest = Node(dest)
            edge = Edge(dest, weight)
            if edge in self.graph[source]:
                continue
            self.graph[source].append(edge)

    def dfs(self, s: Node):
        print(f'Source: {s}')
        self.source = s
        self.reachable = defaultdict(list)
        stack = []
        stack.append(self.source)
        self.source.visited = True
        while stack:
            u = stack.pop()
            print(f'Popped: {u}')
            for adjacent in self.graph[u]:
                v, v_weight = adjacent.v, adjacent.weight
                if not v.visited:
                    print(v, v_weight)
                    v.visited = True
                    stack.append(v)
                    if v in self.reachable[u]:
                        continue
                    self.reachable[u].append(v)
        self.__connected()

    def bfs(self, s: Node):
        print(f'Source: {s}')
        self.source = s
        self.reachable = defaultdict(list)
        queue = PriorityQueue()
        queue.put(self.source)
        self.source.visited = True
        while queue.qsize():
            u = queue.get()
            print(f'Dequeued: {u}')
            for adjacent in self.graph[u]:
                v, v_weight = adjacent.v, adjacent.weight
                if not v.visited:
                    print(v, v_weight)
                    v.visited = True
                    queue.put(v)
                    if v in self.reachable[u]:
                        continue
                    self.reachable[u].append(v)
        self.__connected()

    def dijsktra(self, s: Node):
        print(f'Source: {s}')
        self.source = s
        self.dist = {k: math.inf for k in self.graph.keys()}
        self.dist[source] = 0
        self.previous = {}
        queue = PriorityQueue()
        queue.put(self.source)
        self.source.visited = True
        while queue.qsize():
            u = queue.get()
            # print(f'Dequeued: {u}')
            for adjacent in self.graph[u]:
                v, v_weight = adjacent.v, adjacent.weight
                if not v.visited:
                    v.visited = True
                    queue.put(v)
                alt = self.dist[u] + v_weight
                if alt < self.dist[v]:
                    self.dist[v] = alt
                    self.previous[v] = u

    def __connected(self):
        for k, v in self.reachable.items():
            print(f'{k}, {v}')

    def is_reachable(self):
        pass

    def helper(self, node: Node):
        try:
            # print(self.distances[node])
            # path.insert(0, self.previous[node])
            print(self.previous[node], self.dist[node])
            self.helper(self.previous[node])
        except Exception as e:
            pass

    def print_path(self, destination: Node):
        print(f'To: {destination}, cost: {self.dist[destination]}')
        self.helper(destination)

    def print_costs(self):
        for k, v in self.dist.items():
            print(repr(k), v)

    @property
    def nodes(self):
        return self.graph.keys()


if __name__ == '__main__':
    # edges = [(1,2,100),(1,3,4),(3,4,10),(4,5,20),(4,6,2),(2,3,2)]
    # edges = [(1, 3, 4), (1, 2, 100), (3, 4, 10), (4, 5, 20), (4, 6, 2), (10, None, 0)]
    # edges = [(1, 3, 4), (1, 2, 100), (3, 4, 10), (4, 5, 20), (4, 6, 2), (2, 3, 2), (3,5,2)]
    edges = [
        ('a', 'b', 15),
        ('a', 'c', 13),
        ('a', 'd', 5),
        ('b', 'h', 12),
        ('c', 'b', 2),
        ('c', 'f', 6),
        ('c', 'd', 18),
        ('d', 'e', 4),
        ('d', 'i', 99),
        ('e', 'c', 3),
        ('e', 'f', 1),
        ('e', 'g', 9),
        ('e', 'i', 14),
        ('f', 'b', 8),
        ('f', 'h', 17),
        ('g', 'f', 16),
        ('g', 'h', 7),
        ('g', 'i', 10)
    ]

    source = Node('a')
    graph = Graph(edges)
    # graph.dfs(source)
    # graph.bfs(source)
    graph.dijsktra(source)
    # graph.print_path(Node('f'))
    # graph.print_path(Node('b'))
    # graph.print_path(Node('g'))

    for _ in graph.nodes:
        graph.print_path(_)
        print('')

    print('')
