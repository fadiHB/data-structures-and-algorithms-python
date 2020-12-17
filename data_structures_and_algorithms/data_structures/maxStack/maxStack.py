class Node:
    def __init__ (self,data):
        self.data = data
        self.next = None

class Stacks:
    def __init__(self):
        self.top = None

    def push(self,data):
        '''
        method to add a new node to the stack
        '''
        node = Node(data)
        if self.top:
            node.prev = self.top
            node.next = self.top
        self.top = node


    def pop(self):
        if not self.top:
            return 'the stack is already empty ..!!'
        new_top = self.top.prev
        curret = self.top
        removed = self.top.data
        curret.prev = new_top
        self.top = new_top
        return removed

    def peek(self):
        if not self.top:
            return 'the stack is already empty ..!!'
        return self.top.data

    def max(self):
        if not self.top:
            return 'the stack is already empty ..!!'
        print(max)
        while self.top:
            if self.top.data > max:
                max = self.top.data
            self.top = self.top.next
        return max

if __name__ == "__main__":
    my_stack = Stacks()
    my_stack.push(5)
    my_stack.push(20)
    my_stack.push(10)
    my_stack.push(0)
    my_stack.push(7)
    print(my_stack.max())