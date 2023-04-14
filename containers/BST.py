'''
This file implements the Binary Search Tree data structure.
The functions in this file are considerably harder than the functions in the BinaryTree file.
'''

from containers.BinaryTree import BinaryTree, Node


class BST(BinaryTree):
    '''
    The BST is a superclass of BinaryTree.
    '''

    def __init__(self, xs=None):
        super().__init__()
        if xs:
            self.insert_list(xs)

    def __iter__(self):
        if self.root is None:
            return iter([])
        return self.helper_iter__(self.root)

    @staticmethod
    def helper_iter__(node):
        if node.left:
            yield from (BST.helper_iter__(node.left))
        yield node.value
        if node.right:
            yield from (BST.helper_iter__(node.right))

    def __repr__(self):
        return type(self).__name__ + '(' + str(self.to_list('inorder')) + ')'

    def __eq__(self, t2):
        '''
        This method checks to see if the contents of self and t2 are equal.
        The expression `a == b` desugars to `a.__eq__(b)`.

        NOTE:
        We only care about "semantic" equality,
        and not "syntactic" equality.
        That is, we do not care about the tree structure itself,
        and only care about the contents of what the tree contains.

        HINT:
        Convert the contents of both trees into a sorted list,
        then compare those sorted lists for equality.
        '''
        t1 = self.to_list('inorder')
        t2 = self.to_list('inorder')
        if t1 == t2:
            return True
        else:
            return False
 
    def is_bst_satisfied(self):
        '''
        Whenever you implement a data structure,
        the first thing to do is to implement a
        function that checks whether
        the structure obeys all of its laws.
        This makes it possible to automatically
        test whether insert/delete functions
        are actually working.
        '''
        if self.root:
            return BST._is_bst_satisfied(self.root)
        return True

    @staticmethod
    def _is_bst_satisfied(node):
        '''
        Helper function for isBSTsat
        '''
        ret = True
        if node.left:
            if node.value >= BST._find_largest(node.left):
                ret &= BST._is_bst_satisfied(node.left)
            else:
                ret = False
        if node.right:
            if node.value <= BST._find_smallest(node.right):
                ret &= BST._is_bst_satisfied(node.right)
            else:
                ret = False
        return ret

    def insert(self, value):
        '''
        Inserts value into the BST.
        '''
        if self.root:
            return BST._insert(self.root, value)
        else:
            self.root = Node(value)

    @staticmethod
    def _insert(node, value):
        '''
        Will insert node into a BST and will keep it a BST
        '''
        if node.value >= value:
            if node.left:
                return BST._insert(node.left, value)
            else:
                node.left = Node(value)
        if node.value < value:
            if node.right:
                return BST._insert(node.right, value)
            else:
                node.right = Node(value)

    def insert_list(self, xs):
        '''
        Given a list xs, insert each element of xs into self.
        '''
        for x in xs:
            if self.root:
                BST._insert(self.root, x)
            else:
                self.root = Node(x)

    def __contains__(self, value):
        '''
        Recall that `x in tree` desugars to `tree.__contains__(x)`.
        '''
        return self.find(value)

    def find(self, value):
        '''
        Returns whether value is contained in the BST.
        '''
        if self.root is None:
            return None
        else:
            return BST._find(value, self.root)

    @staticmethod
    def _find(value, node):
        '''
        FIXME:
        Implement this function.
        '''
        if node.value == value:
            return True
        if node.value < value:
            if node.right:
                return BST._find(value, node.right)
            else:
                return False
        if node.value > value:
            if node.left:
                return BST._find(value, node.left)
            else:
                return False

    def find_smallest(self):
        '''
        Returns the smallest value in the tree.
        '''
        if self.root is None:
            return None
        else:
            return BST._find_smallest(self.root)

    @staticmethod
    def _find_smallest(node):
        '''
        This is a helper function for find_smallest and
        not intended to be called directly by the user.
        '''
        assert node is not None
        if node.left is None:
            return node.value
        else:
            return BST._find_smallest(node.left)

    def find_largest(self):
        '''
        Returns the largest value in the tree.
        '''
        if self.root is None:
            return None
        else:
            return BST._find_largest(self.root)

    @staticmethod
    def _find_largest(node):
        '''
        This is a helper function for find_largest and
        not intended to be called directly by the user.
        '''
        assert node is not None
        if node.right is None:
            return node.value
        else:
            return BST._find_largest(node.right)

    def remove(self, value):
        '''
        Removes value from the BST.
        If value is not in the BST, it does nothing.
        '''
        if self.root:
            if self.find(value):
                self.root = BST._remove(self.root, value)
                return self.root
            return self.root
        return self.root

    @staticmethod
    def _remove(node, value):
        '''
        Helper function for remove
        '''
        if node is None:
            return node

        if value < node.value:
            node.left = BST._remove(node.left, value)
            return node
        elif value > node.value:
            node.right = BST._remove(node.right, value)
            return node

        if node.value == value:
            if node.left is None and node.right is None:
                node = None
                return node
            if node.left is None:
                holder = node.right
                node = None
                return holder
            elif node.right is None:
                holder = node.left
                node = None
                return holder
            else:
                nextpar = node
                nextnode = node.right
                while nextnode.left is not None:
                    nextpar = nextnode
                    nextnode = nextnode.left
                if nextpar != node:
                    nextpar.left = nextnode.right
                else:
                    nextpar.right = nextnode.right
                node.value = nextnode.value
                return node

    def remove_list(self, xs):
        '''
        Given a list xs, remove each element of xs from self.
        '''
        for x in xs:
            BST.remove(self, x)
