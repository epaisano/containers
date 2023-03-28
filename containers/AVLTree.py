'''
This file implements the AVL Tree data structure.
The functions in this file are considerably harder
than the functions in the BinaryTree and BST files,
but there are fewer of them.
'''

from containers.BinaryTree import BinaryTree, Node
from containers.BST import BST


class AVLTree(BST):
    '''
    FIXME:
    AVLTree is currently not a subclass of BST.
    You should make the necessary changes in the class
    declaration line above
    and in the constructor below.
    '''

    def __init__(self, xs=None):
        '''
        FIXME:
        Implement this function.
        '''
        super().__init__()
        if xs:
            self.insert_list(xs)

    def balance_factor(self):
        '''
        Returns the balance factor of a tree.
        '''
        return AVLTree._balance_factor(self.root)

    @staticmethod
    def _balance_factor(node):
        '''
        Returns the balance factor of a node.
        '''
        if node is None:
            return 0
        return BinaryTree._height(node.left) - BinaryTree._height(node.right)

    def is_avl_satisfied(self):
        '''
        Returns True if the avl tree satisfies that all nodes
        have a balance factor in [-1,0,1].
        '''
        if self.root:
            return AVLTree._is_avl_satisfied(self.root)
        return True

    @staticmethod
    def _is_avl_satisfied(node):
        '''
        FIXME:
        Implement this function.
        '''
        ret = True
        if node.left:
            if AVLTree._balance_factor(node) in {-1, 0, 1}:
                ret &= AVLTree._is_avl_satisfied(node.left)
            else:
                ret &= False
        if node.right:
            if AVLTree._balance_factor(node) in {-1, 0, 1}:
                ret &= AVLTree._is_avl_satisfied(node.right)
            else:
                ret &= False
        return ret

    @staticmethod
    def _left_rotate(node):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly
        different from our class hierarchy,
        however, so you will have to adapt their code.
        '''
        oldsubtree = node
        if node.right:
            newroot = Node(oldsubtree.right.value)
            newroot.left = Node(oldsubtree.value)
            newroot.right = oldsubtree.right.right
            newroot.left.left = oldsubtree.left
            newroot.left.right = oldsubtree.right.left
            return newroot
        else:
            return node

    @staticmethod
    def _right_rotate(node):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is
        fairly different from our class hierarchy,
        however, so you will have to adapt their code.
        '''
        oldsubtree = node
        if node.left:
            newroot = Node(oldsubtree.left.value)
            newroot.right = Node(oldsubtree.value)
            newroot.left = oldsubtree.left.left
            newroot.right.right = oldsubtree.right
            newroot.right.left = oldsubtree.left.right
            return newroot
        else:
            return node

    def insert(self, value):
        '''
        HINT:
        It is okay to add @staticmethod helper functions for this code.
        The code should look very similar to the code for your insert
        function for the BST,
        but it will also call the left and right rebalancing functions.
        '''
        if self.root:
            self.root = AVLTree._insert(self.root, value)
        else:
            self.root = Node(value)

    @staticmethod
    def _insert(node, value):
        '''
        Will insert node into an AVLTree and will keep it an AVLTree
        '''
        # recursive part // adding in node
        if not node:
            return Node(value)
        elif value < node.value:
            node.left = AVLTree._insert(node.left, value)
        else:
            node.right = AVLTree._insert(node.right, value)
 
        # checking if satisfies AVL condition:
        if AVLTree._balance_factor(node) < -1:
            if value > node.right.value:
                return AVLTree._left_rotate(node)
            else:
                node.right = AVLTree._right_rotate(node.right)
                return AVLTree._left_rotate(node)
        if AVLTree._balance_factor(node) > 1:
            if value < node.left.value:
                return AVLTree._right_rotate(node)
            else:
                node.left = AVLTree._left_rotate(node.left)
                return AVLTree._right_rotate(node)
        return node

    def insert_list(self, xs):
        '''
        Given a list xs, insert each element of xs into self.
        '''
        for x in xs:
            if self.root:
                self.root = AVLTree._insert(self.root, x)
            else:
                self.root = Node(x)

    @staticmethod
    def _rebalance(node):
        '''
        There are no test cases for the rebalance function,
        so you do not technically have to implement it.
        But both the insert function needs the rebalancing code,
        so I recommend including that code here.
        '''
        # if balance factor is negative
        if AVLTree._balance_factor(node) < 0:
            # if they have different signs,
            # then we will want to rotate two times
            # a right rot followed by left
            if AVLTree._balance_factor(node.right) > 0:
                AVLTree._right_rotate(node.right)
                AVLTree._left_rotate(node)
            # if they are both negative,
            # then left rotation is all that's needed
            else:
                AVLTree._left_rotate(node)
        # if balance factor is positive
        elif AVLTree.balance_factor(node) > 0:
            # if balance factor of our change is
            # negative (i.e.: diff signs)
            if AVLTree.balance_factor(node.left) < 0:
                AVLTree._left_rotate(node.left)
                AVLTree._right_rotate(node)
            # if BF of node and newpar are same sign (both pos),
            # then we only want a single rightrot
            else:
                AVLTree._right_rotate(node)
