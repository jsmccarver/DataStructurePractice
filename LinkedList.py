class Node:
    def __init__(self, value):
        self.value = value;
        self.next = None;

    
class LinkedList:
    def __init__(self):
        self.head = None
        
    def __repr__(self):
        nodes = []
        current = self.head
        while current:
            nodes.append("%s" % current.value)
            current = current.next;
        return '->'.join(nodes)          
            
    def add(self, value):
        new_node = Node(value);
        new_node.next = self.head;
        self.head = new_node;
        
