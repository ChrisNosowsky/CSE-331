"""
Project 4: Chris Nosowsky
This project implements a heap class that uses priority queue, either max or min heap based upon the comparison funct.
Builds a tree that is either balanced by max priority or min
"""


class Heap:
    """
    A heap-based priority queue
    Items in the queue are ordered according to a comparison function
    """

    def __init__(self, comp):
        """
        Constructor
        :param comp: A comparison function determining the priority of the included elements
        """
        self.comp = comp
        self.chart = []  # starting table
        # Added Members

    def __len__(self):
        """
        Finds the number of items in the heap
        :return: The size
        """
        return len(self.chart)  # returns the length of chart

    def peek(self):
        """
        Finds the item of highest priority
        :return: The item item of highest priority
        """
        if self.is_empty():  # self is empty then raise index error
            raise IndexError
        item = self.chart[0]  # first item(highest priority)
        return item  # return that highest priority item

    def insert(self, item):
        """
        Adds the item to the heap
        :param item: An item to insert
        """
        self.chart.append(item)  # appends the item to the chart and up heaps
        self.up_heap(len(self) - 1)

    def extract(self):
        """
        Removes the item of highest priority
        :return: the item of highest priority
        """
        if self.is_empty():
            raise IndexError
        self.__swap(0, len(self.chart) - 1)  # swaps with next highest priority item
        item = self.chart.pop()  # pops the chart
        self.down_heap(0)  # down heaps
        return item

    @staticmethod
    def parent(j):
        """
        Gets the parent
        :param j: position
        :return: parent
        """
        return (j - 1) // 2

    def left_child(self, j):
        """
        Gets the left child
        :param j: position
        :return: left child
        """
        child = 2 * j + 1  # this gets the left most child
        if child > len(self.chart) - 1:
            return None
        return child

    def right_child(self, j):
        """
        Gets the right child
        :param j: position
        :return: right child
        """
        child = 2 * j + 2  # this gets the right most child
        if child > len(self.chart) - 1:
            return None
        return child

    def has_right(self, j):
        """
        Checks to see if it has a right child
        :param j: position
        :return: bool stating if it has right
        """
        return self.right_child(j) is not None

    def has_left(self, j):
        """
        Checks to see if it has a left child
        :param j: position
        :return: bool stating if it has left
        """
        return self.left_child(j) is not None

    def down_heap(self, j):
        """
        Heap down until it is greater than its parent
        :param j: position
        """
        if self.has_left(j):  # if it has a left child
            left = self.left_child(j)
            small_child = left  # set the small child equal to the left
            if self.has_right(j):  # if it has a right child, then set right and compare the left and right
                right = self.right_child(j)
                if self.comp(self.chart[right], self.chart[left]):  # if right is smaller than left, set small to right
                    small_child = right
            if self.comp(self.chart[small_child], self.chart[j]):
                self.__swap(j, small_child)
                self.down_heap(small_child)

    def up_heap(self, j):
        """
        Heap up until its children are greater than itself
        :param j: position to start heap up
        """
        parent = self.parent(j)
        if j > 0 and self.comp(self.chart[j], self.chart[parent]):  # if self
            self.__swap(j, parent)  # swaps j with parent position
            self.up_heap(parent)  # recurse

    def __swap(self, i, j):
        """
        Swaps positions
        :param i: position 1 initial
        :param j: position 2 next pos to swap
        """
        self.chart[i], self.chart[j] = self.chart[j], self.chart[i]  # just swaps the i and j positions

    def extend(self, seq):
        """
        Adds all elements from the given sequence to the heap
        :param seq: An iterable sequence
        """
        for element in seq:  # for every element in the seq, insert it in the heap
            self.insert(element)

    def replace(self, item):
        """
        Adds the item the to the heap and returns the new highest-priority item
        Faster than insert followed by extract.
        :param item: An item to insert
        :return: The item of highest priority
        """
        self.insert(item)  # insert item then extract. couldn't figure out how else to do this.
        return self.extract()

    def clear(self):
        """
        Removes all items from the heap
        """
        while self.is_empty() is not True:  # clears the items
            self.extract()

    def __iter__(self):
        """
        An iterator for this heap
        :return: An iterator
        """
        if self.is_empty():
            yield iter([])
        for element in self.chart:
            yield element

    # Supplied methods

    def __bool__(self):
        """
        Checks if this heap contains items
        :return: True if the heap is non-empty
        """
        return not self.is_empty()

    def is_empty(self):
        """
        Checks if this heap is empty
        :return: True if the heap is empty
        """
        return len(self) == 0

    def __repr__(self):
        """
        A string representation of this heap
        :return:
        """
        return 'Heap([{0}])'.format(','.join(str(item) for item in self))

    # Added methods


# Required Non-heap member function


def find_median(seq):
    """
    Finds the median (middle) item of the given sequence.
    Ties are broken arbitrarily.
    :param seq: an iterable sequence
    :return: the median element
    """
    if not seq:
        raise IndexError
    seq = sorted(seq)
    l_len = len(seq)
    if l_len % 2 == 0:  # even length, add the two together and divide
        lower = seq[int((l_len-1)/2)]
        upper = seq[int((l_len+1)/2)]
        return int((lower + upper) / 2)
    else:
        return seq[int((l_len-1)/2)]  # if odd then just divide the length to get the median
