# from ../ import LinkedList 

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.neighbors = list()

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = -1

    def insert(self, value):
        node = Node(value)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1

    def append (self,value):
        node = Node(value)
        current = self.head
        if current == None:
            self.insert(value)
        else:
            while current.next:
                current = current.next
            current.next = node
            node.next = None
        self.size += 1

    def __str__(self):
        # current = self.head
        # str1 = ''
        # while current != None:
        #     str1 += f'{{ {current.value} }} -> '
        #     current = current.next
        # str1 += 'NULL'
        # return str1


class Graph:
    # def __init__(self):
    #     '''
    #     An adjacency list is a collection of linked lists that lists all of the other vertices that are connected.
    #     '''
    #     self.adjacency_list = []

    def __init__(self):
        self.adjacency_list = {}



    # def add_node(self, value):
    #     ll = LinkedList()
    #     node = Node(value)
    #     ll.append(value)
    #     self.adjacency_list.append(ll)
    #     return node

    def add_node(self, value):
        node = Node(value)
        self.adjacency_list[node] = []
        return node

    def add_edge(self, start_node, end_node, weight=1):

        itter_adjacency_list = self.adjacency_list.__iter__()

        while True:
            try:
                current = itter_adjacency_list.__next__().head
                if current.value == start_node.value:
                    neighbor = (end_node, weight)
                    current.neighbors.append(neighbor)
                    break
                
            except:
                raise KeyError('does not exist.')

    def get_nodes(self):
        return self.adjacency_list.keys()


    def size(self):
        return len(self.adjacency_list)

    # for the first level
    def get_neighbors(self, vertex):
        for ll in self.adjacency_list:
            print(ll)
            if ll.head.value == vertex.value:
                return ll.head.neighbors
            

        # return self.adjacency_list[vertex]

if __name__=='__main__':
    my_graph = Graph()
    node1 = my_graph.add_node(5)
    node11 = my_graph.add_node(10)
    node12 = my_graph.add_node(15)
    node111 = my_graph.add_node(20)

    # print(my_graph.adjacency_list)
    my_graph.add_edge(node1, node11)
    my_graph.add_edge(node1, node12)

    my_graph.add_edge(node11, node111)

    '''
    5 -> (10) -> (15)
          |
          -->  (20)
    '''

    # print(my_graph.adjacency_list[0].head.neighbors)
    print(my_graph.get_neighbors(node12))
    print(my_graph.size())
    # my_graph.add_edge(node1, node12)
    