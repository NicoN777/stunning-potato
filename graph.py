class Node:
    def __init__(self, data):
        self.data = data
        self.visited = False

    def __str__(self):
        return f'Data: {self.data}, Visited: {self.visited}'

    def __repr__(self):
        return f'Node({self.data})'

    def __eq__(self, other):
        return self.data == other.data

    def __hash__(self):
        return hash(repr(self))



class Graph:
    def __init__(self, n:int, m:int, edges:list):
        self.n = n
        self.m = m
        self.edges = edges
        self.graph = {Node(i):set() for i in range(1,n+1)}
        for _ in edges:
            source, dest, cost = _
            if source in self.graph:
                self.graph[source].add(dest)

        print(self.graph)

    def dfs(self, s:Node):
        print(f'Source: {s}')
        costs = {k:0 for k in self.graph.keys()}
        stack = []
        stack.append(s)
        s.visited = True
        while stack:
            v = stack.pop()
            for u in self.graph[v]:
                print(u)
                previous = v
                if not u.visited:
                    stack.append(u)
                    u.visited = True
                    costs[u] = costs[v] + 6

        print(costs)





if __name__ == '__main__':

    n = 6
    m = 5
    edges = [(Node(1), Node(2), 100), (Node(1), Node(3), 4), (Node(3), Node(4), 10), (Node(4), Node(5), 20), (Node(4), Node(6), 2)]

    graph = Graph(n,5, edges)
    graph.dfs(Node(1))
    print('Bye')