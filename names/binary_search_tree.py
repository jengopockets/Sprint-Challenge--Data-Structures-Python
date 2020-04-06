class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def insert(self, value):

        if not self.left and value < self.value:
            self.left = BinarySearchTree(value)

        elif not self.right and value >= self.value:
          self.right = BinarySearchTree(value)


        elif value < self.value:
          self.left.insert(value)

        elif value >= self.value:
          self.right.insert(value)


    def contains(self, target):

        if self.value == target:
            return True
        elif target < self.value and self.left:
            return self.left.contains(target)
        elif target >= self.value and self.right:
            return self.right.contains(target)
        elif target < self.value and not self.left:
            return False
        elif target >= self.value and not self.right:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        # Go right until you can go right no further
        if not self.right:
            return self.value
        else:
            return self.right.get_max()


    def for_each(self, cb):
        self.value = cb(self.value)
        
        if self.left and self.right:
            self.left = self.left.for_each(cb)
            self.right = self.right.for_each(cb)

        elif self.left:
            self.left = self.left.for_each(cb)

        elif self.right:
            self.right = self.right.for_each(cb)