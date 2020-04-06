from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        #Check to make sure storage length is not over  capacity
        if self.storage.length < self.capacity:
            #Add to tail
            self.storage.add_to_tail(item)
            #Switch current
            self.current = self.storage.tail
        #If storage is at capacity
        if self.storage.length == self.capacity:
            #Make current new item
            self.current.value = item
            #Move current item to the head if it is the tail
            if self.current is self.storage.tail:
                self.current = self.storage.head
            #Move to next item
            else:
                self.current = self.current.next

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        #Starts with Head
        current = self.storage.head
        while current:
            #Adds to list
            list_buffer_contents.append(current.value)
            #Moves on
            current = current.next
        

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
