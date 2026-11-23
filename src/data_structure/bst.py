class TreeNode:
    def __init__(self,data,left=None,right=None):
        self.left = left
        self.right = right
        self.data = data
class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.count = 0

    def insert(self, data):
        if self.root is None:
            self.root = TreeNode(data)
            self.count += 1
            return True

        current = self.root
        while True:
            if data.item_id == current.data.item_id:
                return False
            elif data.item_id < current.data.item_id:
                if current.left is None:
                    current.left = TreeNode(data)
                    self.count += 1
                    return True
                current = current.left
            else:
                if current.right is None:
                    current.right = TreeNode(data)
                    self.count += 1
                    return True
                current = current.right

    def search(self, item_id):
        current = self.root
        while current is not None:
            if item_id == current.data.item_id:
                return current.data
            elif item_id < current.data.item_id:
                current = current.left
            else:
                current = current.right
        return None

    def delete(self, item_id):
        if self.search(item_id) is None:
            return False
        self.root = self.delete_node(self.root, item_id)
        self.count -= 1
        return True

    def delete_node(self, node, id):
        if node is None:
            return None

        if id < node.data.item_id:
            node.left = self.delete_node(node.left, id)
        elif id > node.data.item_id:
            node.right = self.delete_node(node.right, id)
        else:
            if node.left is None and node.right is None:
                return None

            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            m = node.right
            while m.left is not None:
                m = m.left
            node.data = m.data
            node.right = self.delete_node(node.right, m.data.item_id)
        return node

    def in_order(self):
        lst = []
        self.in_order_helper(self.root, lst)
        return lst

    def in_order_helper(self, n, lst):
        if n is None:
            return
        self.in_order_helper(n.left, lst)
        lst.append(n.data)
        self.in_order_helper(n.right, lst)

    def pre_order(self):
        _list = []
        self.pre_order_helper(self.root, _list)
        return _list

    def pre_order_helper(self, n, lst):
        if n is None:
            return
        lst.append(n.data)
        self.pre_order_helper(n.left, lst)
        self.pre_order_helper(n.right, lst)

    def post_order(self):
        lst = []
        self.post_order_helper(self.root, lst)
        return lst

    def post_order_helper(self, n, lst):
        if n is None:
            return
        self.post_order_helper(n.left, lst)
        self.post_order_helper(n.right, lst)
        lst.append(n.data)

    def is_empty(self):
        return self.root is None

    def size(self):
        return self.count