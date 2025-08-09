class TreeNode:
    def __init__(self, price):
        self.price = price
        self.left = None
        self.right = None

class PriceBST:
    def __init__(self):
        self.root = None

    def insert(self, price):
        if not self.root:
            self.root = TreeNode(price)
        else:
            self._insert_rec(self.root, price)

    def _insert_rec(self, node, price):
        if price < node.price:
            if node.left is None:
                node.left = TreeNode(price)
            else:
                self._insert_rec(node.left, price)
        else:
            if node.right is None:
                node.right = TreeNode(price)
            else:
                self._insert_rec(node.right, price)

    def search(self, price):
        return self._search_rec(self.root, price)

    def _search_rec(self, node, price):
        if node is None or node.price == price:
            return node
        if price < node.price:
            return self._search_rec(node.left, price)
        return self._search_rec(node.right, price)
