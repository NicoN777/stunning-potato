from collections import defaultdict
from queue import PriorityQueue

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
    def __init__(self, v:Node, weight:int):
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
    def __init__(self, edges:list):
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

    def dfs(self, s:Node):
        # print(f'Source: {s}')
        self.source = s
        self.costs = {k:0 for k in self.graph.keys()}
        stack = []
        stack.append(self.source)
        s.visited = True
        while stack:
            current = stack.pop()
            # print('POP', current)
            for _ in self.graph[current]:
                adjacent, weight = _.v, _.weight
                # print('***', adjacent, weight)
                if not adjacent.visited:
                    stack.append(adjacent)
                    adjacent.visited = True
                    self.costs[adjacent] = self.costs[current] + weight

    def bfs(self, s:Node):
        # print(f'Source: {s}')
        self.source = s
        self.costs = {k: 0 for k in self.graph.keys()}
        queue = PriorityQueue()
        queue.put(self.source)
        s.visited = True
        while queue.qsize():
            current = queue.get()
            # print('DEQUEUE', current)
            for _ in self.graph[current]:
                adjacent, weight = _.v, _.weight
                # print('***', adjacent, weight)
                if not adjacent.visited:
                    queue.put(adjacent)
                    adjacent.visited = True
                    self.costs[adjacent] = self.costs[current] + weight

    def reachable(self):
        return [k for k, v in self.costs.items() if v > 0]

    def unreachable(self):
        self.costs.pop(self.source)
        return [k for k, v in self.costs.items() if v <= 0]

    def print(self):
        print('Node  --> Adjacent(s)')
        for k, v in self.graph.items():
            print(k, ' --> ', v)

    def print_costs(self):
        print(f'From Source: {self.source}')
        self.costs.pop(self.source)
        print(self.costs)


if __name__ == '__main__':
    edges = [(1,2,100),(1,3,4),(3,4,10),(4,5,20),(4,6,2), (8, 9, 100)]
    graph = Graph(edges)
    graph.print()
    graph.dfs(Node(1))
    # graph.dfs(Node(8))
    del graph
    graph = Graph(edges)
    graph.bfs(Node(1))
    # graph.bfs(Node(8))
    graph.print_costs()
    print('Bye')