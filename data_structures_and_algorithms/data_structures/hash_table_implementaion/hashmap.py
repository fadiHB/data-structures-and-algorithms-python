class Node:
    def __init__(self, indx, value):
        self.indx = indx
        self.value = value
        self.next = None
        
    
class Linked_list:
    def __init__(self):
        self.head = None

    def insert(self, node):
        if not self.head:
            self.head = node
        node.next = self.head
        self.head = node

    def value(self):
        lst = []

        if self.head is None:
            return 'link list is Empty'

        temp = self.head
        while temp:
            lst.append(temp.value)
            temp = temp.next

        if len(lst) == 1:
            return lst[0]
        return lst


class Hashmap:
    def __init__(self,size):
        self.size = size
        self.map = [None]*size
        self.linked_list = Linked_list()

    def get_hash (self,key):
        ascii_total = 0
        for ch in key:
            ascii_total += ord(ch)
        hashed = (ascii_total * 17) % self.size
        return hashed

    def add (self,key, value):
        indx = self.get_hash(key)
        node = Node(indx,value)
        if not self.map[indx]:
            ll = Linked_list()
            ll.insert(node)
            self.map[indx] = ll
            return
        self.map[indx].insert(node)
        #self.map[indx].next = node




if __name__=='__main__':
    things = Hashmap(1024)
    things.add('name', 'Ahmad')
    # things.add('color', 'red')
    # things.add('num', 3)
    # assert things.find('color') == 'red'
    # assert things.find('num') == 3
    things.add('could', 67)
    things.add('cloud', 34)
    things.add('coldu', 344)
    # assert ['could', 67] in things.map[things.get_hash('could')]
    # assert ['cloud', 34] in things.map[things.get_hash('cloud')]
    # assert ['coldu', 344] in things.map[things.get_hash('coldu')]
    print('------- indx -------')
    print(things.get_hash('could'))
    print(things.get_hash('cloud'))
    print(things.get_hash('coldu'))
    print('--------------------')

    #print(things.map)
    idx = things.get_hash('name')
    ll = things.map[idx]
    val = ll.value()

    # print(idx)
    # print(ll)
    print(val)
    # print(things.map[things.get_hash('name')].value())
    # print(things.map[things.get_hash('could')].value())



    print('TESTED Successfully!!!!!')
