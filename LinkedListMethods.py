class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.lenght = 0
    
    def __str__(self):
        temp_node = self.head 
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next

        return result
    
    def preapend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node


        self.lenght +=1
            

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.lenght += 1
    
    def insertValue (self, value, index):
        new_node = Node(value)
        if index < 0 or index > self.lenght:
            return False
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            
            new_node.next = temp_node.next
            temp_node.next = new_node
            self.lenght += 1
            return True
        
    def traverse(self):
        current_node = self.head
        while current_node: # python way means current_node is not None
            print(current_node.value)
            current_node = current_node.next
        
    def search_node(self, target):
        current_node = self.head
        i = 0
        while current_node:
            if current_node.value == target: 
                return print(i)
            current_node = current_node.next
            i+=1
        print(-1)
    
    def get_value(self, index):
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        
        return print(current_node.value)
    
    def set_value(self, index, value):
        current_node = self.head 
        for _ in range(index):
            current_node = current_node.next
        
        current_node.value = value
        return True 
    
    def pop_first(self):
        popped_element = self.head
        if self.lenght == 0:
            return None
        if self.lenght == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popped_element.next = None
        self.lenght -= 1
        return popped_element.value
    
    def pop_last(self):
        popped_element = self.tail
        temp_node = self.head
        if self.lenght == 0:
            return None
        if self.lenght == 1:
            self.head = None
            self.tail = None
        else: 
            while temp_node.next is not self.tail:
                temp_node = temp_node.next
            self.tail = temp_node
            temp_node.next = None
            self.lenght -= 1
            return popped_element.value
        
    def pop_element(self, index):
        popped_node = index
        temp_node = self.head 
        if self.lenght == 0:
            return None
        if self.lenght == 1:
            self.head = None 
            self.tail = None
            self.lenght -=1 
        else:
            for _ in range(index-1):
                temp_node = temp_node.next

            popped_node = temp_node.next
            temp_node.next = popped_node.next
            popped_node.next = None
            self.lenght -= 1

    def delete_all(self):
        self.head = None
        self.tail = None
        self.lenght = 0     

    

new_linked_list = LinkedList()
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.append(30)
new_linked_list.append(40)
new_linked_list.preapend(5)
new_linked_list.preapend(3)
new_linked_list.insertValue(35, 5)
new_linked_list.insertValue(1,0)
#print(new_linked_list.lenght)
#print(new_linked_list.tail.value)
print(new_linked_list)
#new_linked_list.traverse()
new_linked_list.search_node(30)
new_linked_list.get_value(5)
new_linked_list.set_value(2,7)
print(new_linked_list.pop_first())
print(new_linked_list.pop_last())
print(new_linked_list)
new_linked_list.pop_element(3)
