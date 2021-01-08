class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        
class Hashmap:
    def __init__(self,size):
        self.size = size
        self.map = [None]*size

    def get_hash (self,key):
        ascii_total = 0
        for ch in key:
            ascii_total += ord(ch)
        hashed = (ascii_total * 17) % self.size
        return hashed

    def add (self,key, value):
        indx = self.get_hash(key)
        node = Node(key,value)
        if not self.map[indx]:
            self.map[indx] = node
            return
        self.map[indx].next = node

    def get(self,key):
        indx = self.get_hash(key)
        while self.map[indx]:
            if self.map[indx].key == key:
                return self.map[indx].value
            self.map[indx] = self.map[indx].next

    def contains(self,key):
        indx = self.get_hash(key)
        while self.map[indx]:
            if self.map[indx].key == key:
                return True
            self.map[indx] = self.map[indx].next
        return False





if __name__=='__main__':
    pass
