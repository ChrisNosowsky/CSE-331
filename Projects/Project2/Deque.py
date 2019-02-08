"""
Project 2: Chris Nosowsky
"""
class Node:
    """Node Class"""
    def __init__(self, value, next_node=None):
        """
        initializes value and next node
        """
        self.value = value  # element at the node
        self.next_node = next_node  # reference to next node
    def __eq__(self, other):
        """
        Checks for equality.
        """
        if other is None:  # if none doesn't exist
            return False
        if self.value == other.value:  # if they are equal
            return True
        return False
    def __repr__(self):
        """
        returns the string version of Node data.
        """
        return str(self.value)  # string representation of self(the node)
class Deque:
    """
    A double-ended queue
    """
    def __init__(self):
        """
        Initializes an empty Deque
        """
        self.front = None  # Front monitoring
        self.back = None  # Back monitoring
        self.size = 0  # Size of the deque
    def __len__(self):
        """
        Computes the number of elements in the Deque
        :return: The size of the Deque
        """
        return self.size  # return the size of the deque
    def peek_front(self):
        """
        Looks at, but does not remove, the first element
        :return: The first element
        """
        if self.front is not None:  # if the front is not none, look at the front value; otherwise IndexError
            return self.front.value

        raise IndexError
    def peek_back(self):
        """
        Looks at, but does not remove, the last element
        :return: The last element
        """
        if self.back is not None:  # Looks at the back value(data), if it's None, then raise an IndexError
            return self.back.value
        raise IndexError
    def push_front(self, e):
        """
        Inserts an element at the front of the Deque
        :param e: An element to insert
        """
        if self.size == 0:  # If the size is 0, create a new node and insert for the front and back and increase size
            new_node = Node(e, self.front)
            self.front = new_node
            self.back = new_node
            self.size += 1
        else: # if not a new deque, insert at the front and increase size
            self.front = Node(e, self.front)
            self.size += 1
    def push_back(self, e):
        """
        Inserts an element at the back of the Deque
        :param e: An element to insert
        """
        if self.size == 0:  # if the size is zero, create a new node and set them equal to the front and back.
            new_node = Node(e)
            self.front = new_node
            self.back = new_node
            self.size += 1
        else:  # Else set the new node to backs next node and then set the back to the new node. Increase size
            new_node = Node(e)
            self.back.next_node = new_node
            self.back = new_node
            self.size += 1
    def pop_front(self):
        """
        Removes and returns the first element
        :return: The (former) first element
        """
        front = self.front
        if front is not None:  # If the front is not none, then pop the front. Front becomes its next node.
            next_node = self.front.next_node
            self.front = next_node
            self.size -= 1
            return front.value  # Old front element val
        raise IndexError
    def pop_back(self):
        """
        Removes and returns the last element
        :return: The (former) last element
        """
        if self.front is None:
            raise IndexError
        current_node = self.front
        prev_node = None
        while current_node.next_node is not None:  # This is wrong. I needed a prev node for the back.
            prev_node = current_node
            current_node = current_node.next_node
        if prev_node is None:  # If the prev node was None, then the front and back will be set to None. Size 0
            self.front = None
            self.back = None
            self.size -= 1
        else:  # Else pop the back and set the back to the prev_node
            prev_node.next_node = None
            self.back = prev_node
            self.size -= 1
        return current_node.value
    def clear(self):
        """
        Removes all elements from the Deque
        """
        front = self.front
        while front is not None:  # Goes through every element starting from front and removes it
            next_node = self.front.next_node
            self.front = next_node
            self.size -= 1
            front = self.front
        self.back = None
    def __iter__(self):
        """
        Iterates over this Deque from front to back
        :return: An iterator
        """
        traverse = self.front
        while traverse is not None:  # Goes through every element and reads(yield) over it
            yield traverse.value
            traverse = traverse.next_node
    def extend(self, other):
        """
        Takes a Deque object and adds each of its elements to the back of self
        :param other: A Deque object
        """
        traverse = other.front
        while traverse is not None:  # Until you read the end of the other, keep adding it to the back of self
            if self.size == 0:
                self.front = traverse
                self.back = traverse
                self.size += 1
            else:
                self.back.next_node = traverse
                self.back = traverse
                self.size += 1
            traverse = traverse.next_node
        other.back = None
    def drop_between(self, start, end):
        """
        Deletes elements from the Deque that within the range [start, end)
        :param start: indicates the first position of the range
        :param end: indicates the last position of the range(does not drop this element)
        """
        count = 0
        temp = self.front
        prev = self.front
        if end > len(self) or start < 0:  # If end is greater then length of self or if the start is less then index 0
            raise IndexError
        if start > end:  # if the end is less then the start(weird)
            raise IndexError
        while temp is not None:  # this increases in count until its in the start and end range, then starts deleting
            if start <= count < end:
                prev.next_node = temp.next_node
                temp = temp.next_node
                self.size -= 1
            else:
                prev = temp
                temp = temp.next_node
            count += 1
            if count == end:
                break
    def count_if(self, criteria):
        """
        counts how many elements of the Deque satisfy the criteria
        """
        count = 0
        traverse = self.front
        while traverse is not None:  # If the criteria is true, increase count. Keep going through every element
            if criteria(traverse.value):
                count += 1
            traverse = traverse.next_node
        return count
    def is_empty(self):
        """
        Checks if the Deque is empty
        :return: True if the Deque contains no elements, False otherwise
        """
        return len(self) == 0
    def __repr__(self):
        """
        A string representation of this Deque
        :return: A string
        """
        return 'Deque([{0}])'.format(','.join(str(item) for item in self))
