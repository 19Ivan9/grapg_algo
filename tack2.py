class Dijkstra:
    def __init__(self):
        self.__graph = {}
        self.__start_node = None
        self.__end_node = None

    def addg(self, first_node, second_node, distance):
        if distance <= 0:
            raise ValueError('Err')
        self.__graph[f'{first_node}:{second_node}'] = distance
        self.__graph[f'{second_node}:{first_node}'] = distance

    @property
    def nodes(self):
        return list(set(i.split(':')[0] for i in self.__graph))

    @property
    def start(self):
        return self.__start_node

    @start.setter
    def start(self, value):
        if value not in self.nodes:
            raise ValueError('Value dosn\'t exist!')
        self.__start_node = value
        self.__recalculate()

    def __recalculate(self):
        self.distances = {i: None for i in self.nodes}
        self.distances[self.start] = 0
        queue = [self.start]

        while queue:
            node = queue.pop(0)

            for i in self.get_neighbour(node):
                d1 = self.distances[node] + self.get_distance(node, i)
                if self.distances[i] is None or self.distances[i] > d1:
                    self.distances[i] = d1
                    queue.append(i)

    def get_neighbour(self, node):
        return [i.split(':')[1] for i in self.__graph if i.split(':')[0] == node]

    def get_distance(self, first_node, second_node):
        return self.__graph[f'{first_node}:{second_node}']

    @property
    def end(self):
        return self.__end_node

    @end.setter
    def end(self, node):
        if node not in self.nodes:
            raise ValueError('Value dosn\'t exist!')
        self.__end_node = node

    @property
    def distance(self):
        if not self.start:
            raise ValueError('No last position')
        if not self.end:
            raise ValueError('No last position')
        road = [self.end]
        queue = [self.end]
        while queue:
            node = queue.pop(0)
            for i in self.get_neighbour(node):
                if self.distances[node] - self.get_distance(node, i) == self.distances[i]:
                    road.append(i)
                    queue.append(i)
        return road[::-1]


if __name__ == '__main__':
    g = Dijkstra()
    g.addg('A', 'B', 2)
    g.addg('A', 'C', 4)
    g.addg('B', 'D', 1)
    g.addg('C', 'D', 2)
    g.addg('C', 'E', 6)
    g.addg('D', 'E', 4)
    print(g.nodes)
    # g.start = 'Z'
    g.start = 'A'
    g.end = 'E'
    # print(g.distances)
    # print(g.get_neighbour('A'))
    print(g.distance)
    graph = {
        'A': {'B': 2, 'C': 4},
        'B': {'A': 2, 'C': 3, 'D': 8},
        'C': {'A': 4, 'B': 3, 'E': 5, 'D': 2},
        'D': {'B': 8, 'C': 2, 'E': 11, 'F': 22},
        'E': {'C': 5, 'D': 11, 'F': 1},
        'F': {'D': 22, 'E': 1},
    }
