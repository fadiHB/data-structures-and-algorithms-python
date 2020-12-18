class Node:
    def __init__(self, data):
      self.data = data
      self.next = None

class Stacks:
    def __init__(self):
        self.top = None
        self.size = 0

    def push (self,data):
        node = Node(data)
        if not self.top:
            self.top = node
            self.size += 1
            return
        node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):
        if not self.top:
            return 'stacks is empty'
        self.top = self.top.next
        self.size -= 1

    def peek(self):
        if self.top:
            return self.top.data
        return 'stacks is empty'


def isBalanced(str):
    my_stacks = Stacks()
    for i in str:
        if i == '{' or i == '(' or i == '[':
            my_stacks.push(i)
            continue
        if i ==')' and my_stacks.top.data == '(':
            my_stacks.pop()
            continue
        if i ==')' and my_stacks.top.data != '(':
            return False
        if i ==']' and my_stacks.top.data == '[':
            my_stacks.pop()
            continue
        if i ==']' and my_stacks.top.data != '[':
            return False
        if i =='}' and my_stacks.top.data == '{':
            my_stacks.pop()
            continue
        if i =='}' and my_stacks.top.data != '{':
            return False
    return my_stacks.size == 0
    
if __name__ == "__main__":
    print(isBalanced('({[}])'))