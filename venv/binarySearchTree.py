class Node(object):

    def __init__(self, data=None, left=None, right=None, parent=None):
        self.left = left
        self.right = right
        self.parent = parent
        self.data = data

    def set_left_node(self, lnode):
        """
        Set left node
        :param lnode:
        :return:
        """
        self.left = lnode

    def set_right_node(self, rnode):
        """
        Set right node
        :param rnode:
        :return:
        """
        self.right = rnode

    def set_parent_node(self, pnode):
        """
        Set parent node
        :param pnode:
        :return:
        """
        self.parent = pnode

    def set_data(self, data):
        """
        Set data
        :param data:
        :return:
        """
        self.data = data

    def get_left_node(self):
        """
        Get left node
        :return:
        """
        return self.left

    def get_right_node(self):
        """
        Get right node
        :return:
        """
        return self.right

    def get_parent_node(self):
        """
        Get parent node
        :return:
        """
        return self.parent

    def get_data(self):
        """
        Get data
        :return:
        """
        return self.data


class BST(object):

    def __init__(self, root=None):
        self.root = root

    def get_root(self):
        """
        Get root node
        :return:
        """
        return self.root

    def set_root(self, root):
        """
        Set root node
        :param root:
        :return:
        """
        self.root = root

    def insert(self, data):
        """
        Insert a node to binary search tree
        :param data:
        :return:
        """
        x = self.get_root()
        y = None  # parent of x
        while x:  # find place where new node to be inserted
            y = x
            if data < x.get_data():
                x = x.get_left_node()
            else:
                x = x.get_right_node()

        new_node = Node(data)
        new_node.set_parent_node(y)

        if not y:  # new_node is the root
            self.set_root(new_node)
        elif data < y.get_data():
            y.set_left_node(new_node)
        else:
            y.set_right_node(new_node)

    def inorder_walk(self, x):
        """
        Inorder tree walk. BST should be sorted
        :param x:
        :return:
        """
        if x:
            self.inorder_walk(x.get_left_node())
            print(x.get_data())
            self.inorder_walk(x.get_right_node())

    def search(self, x, k):
        """
        Search a key in BST
        :param x:
        :param k:
        :return:
        """
        if not x or k == x.get_data():
            return x
        if k < x.get_data():
            return self.search(x.get_left_node(), k)
        else:
            return self.search(x.get_right_node(), k)

    def minimum(self, x):
        """
        Find minimum node of x
        :param x:
        :return:
        """
        if not x:
            return None
        if not x.get_left_node():
            return x
        while x.get_left_node():
            x = x.get_left_node()
        return x

    def maximum(self, x):
        """
        Find maximum node of x
        :param x:
        :return:
        """
        if not x:
            return None
        if not x.get_right_node():
            return x
        while x.get_right_node():
            x = x.get_right_node()
        return x

    def successor(self, x):
        """
        Find successor of x: smallest item > x
        :param x:
        :return:
        """
        if not x or not x.get_right_node():
            return None
        # Successor is the smallest in right subtree
        if x.get_right_node():
            return self.minimum(x.get_right_node())
        # Successor is the node whose left child is parent(x)
        y = x.get_parent_node()
        while y and x == y.get_right_node():
            x = y
            y = y.get_parent_node()
        return y


print("-------------------------- Insert node to BST ------------------------")
bst = BST()
bst.insert(5)
bst.insert(3)
bst.insert(6)
bst.insert(7)
bst.insert(8)

print("BST Inorder------------")
bst.inorder_walk(bst.get_root())

print("BST Search node------------")
print(bst.search(bst.get_root(), 7).get_data())

print("BST minimum item starting from root")
print(bst.minimum(bst.get_root()).get_data())

print("BST maximum item starting from root")
print(bst.maximum(bst.get_root()).get_data())

print("BST successor item starting from root")
print(bst.successor(bst.get_root(), ).get_data())