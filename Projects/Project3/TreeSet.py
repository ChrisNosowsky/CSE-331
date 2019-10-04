"""
Project 3: Chris Nosowsky
This project implements TreeNode class to build a TreeSet that builds a AVL tree that
rebalances and does rotations based on the balance factor. Other functions implemented in order to build a stable tree
"""


class TreeNode:
    """
    A TreeNode to be used by the TreeSet
    """

    def __init__(self, data):
        """
        Constructor
        You can add additional data as needed
        :param data:
        """
        self.data = data
        self.left = None
        self.right = None
        # added stuff below
        self.parent = None
        self.height = -1

    def __repr__(self):
        """
        A string representing this node
        :return: A string
        """
        return 'TreeNode({0})'.format(self.data)


class TreeSet:
    """
    A set data structure backed by a tree.
    Items will be stored in an order determined by a comparison
    function rather than their natural order.
    """

    def __init__(self, comp):
        """
        Constructor for the tree set.
        You can perform additional setup steps here
        :param comp: A comparison function over two elements
        """
        self.comp = comp
        # added stuff below
        self.root = None
        self.size = 0
        self.lst = list()
        self.unlock = 0  # simply used for the purpose of running the in_order function once

    def __len__(self):  # gets the size of the tree (num elements)
        """
        Counts the number of elements in the tree
        :return:
        """
        return self.size

    def height(self):
        """
        Finds the height of the tree
        :return:
        """
        if self.root is None:
            return -1
        q = list()  # list for appending all the tree nodes
        q.append(self.root)
        height = -1

        while True:
            node_count = len(q)
            if node_count == 0:
                return height  # if there are no elements, -1
            height += 1
            while node_count > 0:  # loop through the node_count and pop off each element. Increments height every time
                node = q[0]
                q.pop(0)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                node_count -= 1  # decrease node_count every time

    def insert(self, item):
        """
        Inserts the item into the tree.
        :param item:
        :return: If the operation was successful
        """
        new_node = TreeNode(item)  # create a new node to add
        if self.root is None:  # first case: empty tree
            self.root = new_node
        else:
            cur = self.root
            while cur is not None:  # this goes through the tree and finds where to put the new node that we want to add
                if self.comp(new_node.data, cur.data) == 0:  # duplicates get ignored
                    return False
                if self.comp(new_node.data, cur.data) < 0:  # search left until no more left, then add
                    if cur.left is None:
                        new_node.parent = cur
                        cur.left = new_node
                        cur = None
                    else:
                        cur = cur.left
                else:  # else go right and add
                    if cur.right is None:
                        new_node.parent = cur
                        cur.right = new_node
                        cur = None
                    else:
                        cur = cur.right
        self.re_balance(self.root, item)  # supposed to balance the tree using the re_balance function
        self.size += 1
        return True

    def re_balance(self, root, item):
        """
        Re balances AVL tree
        :param root
        :param item
        :return: nothing
        """
        cur = root
        while cur is not None:  # this takes a root, loops through each node and checks the height and balance
            cur.height = 1 + max(self.get_height(cur.left), self.get_height(cur.right))
            balance = self.get_balance(cur)
            if cur.left is not None:  # case 1 - left-left
                if balance > 1 and self.comp(item, cur.left.data) < 0:
                    self.right_rotate(cur)
            if cur.right is not None:  # case 2 - right-right
                if balance < -1 and self.comp(cur.right.data, item) < 0:
                    self.left_rotate(cur)
            if cur.left is not None:  # case 3 - left-right
                if balance > 1 and self.comp(cur.left.data, item) < 0:
                    cur.left = self.left_rotate(cur.left)
                    self.right_rotate(cur)
            if cur.right is not None:  # case 4 - right-left
                if balance < -1 and self.comp(item, cur.right.data) < 0:
                    cur.right = self.right_rotate(cur.right)
                    self.left_rotate(cur)
            cur = None  # if we don't enter any of the cases, return None b/c the tree must have only a root

    def remove(self, item):
        """
        Removes the item from the tree
        :param item:
        :return: If the operation was successful
        """
        if self.root is None:
            return False
        par = None  # parent. Will update later for tracking purposes
        cur = self.root  # current
        while cur is not None:  # loops through tree until we find the data that we want to remove
            if cur.data == item:
                if not cur.left and not cur.right:
                    if not par:  # if the parent is not none, set self.root to none
                        self.root = None
                    elif par.left == cur:
                        # if the current is equal to parent left, then we want to delete parents left
                        par.left = None
                    else:
                        par.right = None
                elif cur.left and not cur.right:  # remove one left child
                    if not par:  # node is root:
                        self.root = cur.left
                        cur.left.parent = None
                    elif par.left == cur:
                        par.left = cur.left
                        cur.left.parent = par
                    else:
                        par.right = cur.left
                        cur.left.parent = par

                elif not cur.left and cur.right:  # Remove node with only right child
                    if not par:  # node is root
                        self.root = cur.right
                        cur.right.parent = None
                    elif par.left == cur:
                        par.left = cur.right
                        cur.right.parent = par
                    else:
                        par.right = cur.right
                        cur.right.parent = par

                else:  # Remove node with two children
                        # Find successor (leftmost child of right subtree)
                    suc = self.min(cur.right)
                    self.remove(suc.data)

                    self.size += 1

                    successor_data = TreeNode(suc.data)  # get's the data from the successor and creates new node
                    successor_data.left = cur.left  # sets the left to the current node's left
                    successor_data.right = cur.right
                    successor_data.parent = par

                    if successor_data.left is not None:
                        successor_data.left.parent = successor_data
                    if successor_data.right is not None:
                        successor_data.right.parent = successor_data

                    if cur.parent is not None:  # Assign cur's data with successor_data
                        if cur.parent.left == cur:
                            cur.parent.left = successor_data
                        if cur.parent.right == cur:
                            cur.parent.right = successor_data
                    cur = successor_data

                    if cur.parent is None:  # if there is no parent, set the root be the successor_data
                        self.root = successor_data
                self.size -= 1  # decrease size by one after the remove function is complete
                return True
            elif cur.data < item:  # Search right
                par = cur
                cur = cur.right

            else:  # Search left
                par = cur
                cur = cur.left

        if self.root is None:  # if the root doesn't exist, empty tree, return false.
            return False
        return False

    def min(self, node):
        """
        Min function that finds the absolute min
        :param node
        :return:
        """
        if node is None or node.left is None:  # if the node is none or the left node is none, then there is no min
            return node
        else:
            return self.min(node.left)  # otherwise if there does exist a left side of tree, recurse

    def __contains__(self, item):
        """
        Checks if the item is in the tree
        :param item:
        :return: if the item was in the tree
        """
        temp = self.root
        if temp is None:
            return False
        while temp is not None:  # loops through the tree to see if the tree contains the item we want
            if self.comp(item, temp.data) == 0:  # temp.data == item:
                return True
            if self.comp(item, temp.data) < 0:  # item < temp.data
                if temp.left is None:
                    return False
                else:
                    temp = temp.left
            else:  # else search the right side!
                if temp.right is None:
                    return False
                else:
                    temp = temp.right
        return False

    def right_rotate(self, node):
        """
        Checks if the item is in the tree
        :param node the node to be rotating
        :return: lef the new node
        """
        lef = node.left  # these variables do the right rotation
        t3 = lef.right
        lef.right = node
        node.left = t3
        # update the heights below after the rotation is complete
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        lef.height = 1 + max(self.get_height(node.left), self.get_height(lef.right))
        return lef  # returns the node we performed rotation on

    def left_rotate(self, node):
        """
        Checks if the item is in the tree
        :param node the node to be rotating
        :return: rig the new root
        """
        rig = node.right  # this does the left rotation
        t2 = rig.left
        rig.left = node
        node.right = t2
        # we update the heights below
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        rig.height = 1 + max(self.get_height(rig.left), self.get_height(rig.right))
        return rig

    @staticmethod
    def get_height(root):
        """
        Gets the height at the root
        :param root
        :return:
        """
        if not root:  # if no root exists, then the height is -1
            return -1
        return root.height  # otherwise return the root's height

    def get_balance(self, root):
        """
        Gets the balance factor
        :param root
        :return:
        """
        if not root:  # if the root doesn't exist, then the balance is 0
            return 0

        return self.get_height(root.left) - self.get_height(root.right)  # otherwise figure out the heights

    def clear(self):
        """
        Deletes every node including root
        :param
        :return:
        """
        if self.root is not None:
            self.leaf_delete(self.root)  # this calls leaf_delete which deletes the leafs
            self.root = None  # had an issue of the root not being deleted, so I added this
        self.size = 0  # reset size

    def leaf_delete(self, root):
        """
        Deletes leafs
        :param root
        :return:
        """
        if root is not None:
            self.leaf_delete(root.left)  # recurses deleting all left side leaves
            self.leaf_delete(root.right)  # recurses deleting all right side leaves
            root.left = None
            root.right = None

    def first(self):
        """
        Finds the minimum item of the tree
        :return: the min item
        """
        if self.root is None:
            raise KeyError
        self.in_order(self.root)  # calls in_order to make a set
        min_e = max(self.lst)
        for element in self.lst:  # loops through the set and finds the smallest element in it and returns it
            if self.comp(element, min_e) < 0:
                min_e = element
        return min_e

    def last(self):
        """
        Finds the maximum item of the tree
        :return: the max item
        """
        if self.root is None:
            raise KeyError
        cur = self.root
        if cur.right is None:
            return self.root.data
        if self.comp(self.root.right.data, self.root.data) > 0:
            # compares the right data with the data we are currently looking at. If right is bigger, advance to right
            while cur is not None:
                cur.parent = cur
                if cur.right is None:
                    return cur.parent.data
                cur = cur.right
        else:  # if the compare is reversed, call the self.first() instead
            self.first()
        return cur.parent.data

    def __iter__(self):
        """
        Does an in-order traversal of the tree
        :return:
        """
        if self.root is None:  # if none return an empty iter
            yield iter([])
        if self.unlock == 0:
            self.in_order(self.root)  # runs once every time in the for loop
        for element in self.lst:  # yields the element for user
            yield element

    def in_order(self, root):
        """
        This is an algorithm function that adds to the set in order. So left -> parent -> right
        :param root
        :return: the list
        """
        self.unlock = 1  # this is just for the purpose of running in_order once
        self.lst = []
        if root:
            self.lst = self.in_order(root.left)
            self.lst.append(root.data)  # appends the data to the list
            self.lst = self.lst + self.in_order(root.right)
        return self.lst

    def is_disjoint(self, other):
        """
        Check if two TreeSet is disjoint
        :param other: A TreeSet object
        :return: True if the sets have no elements in common
        """
        self.in_order(self.root)
        other.in_order(other.root)
        s1 = set(self.lst)  # realized i made the data member a list, so I convert it to a set here to use isdisjoint
        s2 = set(other.lst)
        tf = s1.isdisjoint(s2)
        return tf
    # Pre-defined methods

    def is_empty(self):
        """
        Determines whether the set is empty
        :return: False if the set contains no items, True otherwise
        """
        return len(self) == 0

    def __repr__(self):
        """
        Creates a string representation of this set using an in-order traversal.
        :return: A string representing this set
        """
        return 'TreeSet([{0}])'.format(','.join(str(item) for item in self))

    def __bool__(self):
        """
        Checks if the tree is non-empty
        :return:
        """
        return not self.is_empty()
