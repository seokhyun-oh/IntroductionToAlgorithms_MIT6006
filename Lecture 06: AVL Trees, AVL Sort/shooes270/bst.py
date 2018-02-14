class Node:

    def __init__(self, key):
        self.__init__(key, None)

    def __init__(self, key, parent):
        self.key = key
        self.parent = parent
        self.left = None
        self.right = None


class BST:

    def __init__(self):
        self.root = None

    def clear(self):
        self.__clear(self.root)
        self.root = None

    def __clear(self, node):
        if not node:
            return
        self.__clear(node.left)
        self.__clear(node.right)
        del node

    def is_empty(self):
        return self.root is None

    def contains(self, key):
        return self.find(key) is not None

    def find(self, key):
        return self.__find(key, self.root)

    def __find(self, key, node):
        if node is None:
            return
        if key == node.key:
            return node.key
        if key > node.key:
            return self.__find(key, node.right)
        return self.__find(key, node.left)

    def find_max(self):
        if self.root is None:
            print("Tree is empty")
            return
        node = self.root
        while node.right:
            node = node.right
        return node.key

    def find_min(self):
        if self.root is None:
            print("Tree is empty")
            return
        node = self.root
        while node.left:
            node = node.left
        return node.key

    def insert(self, key):
        node = self.__insert(key, self.root)
        if self.root is None:
            self.root = node
        return node

    def __insert(self, key, node, parent=None):
        if node is None:
            return Node(key, parent)
        if key > node.key:
            child = self.__insert(key, node.right, node)
            if child.parent == node:
                node.right = child
        else:
            child = self.__insert(key, node.left, node)
            if child.parent == node:
                node.left = child
        return child

    def print_tree(self):
        self.__print_tree(self.root, 0)

    def __print_tree(self, node, level):
        if node is None:
            return
        self.__print_tree(node.right, level+1)
        print('.'*level, node.key)
        self.__print_tree(node.left, level+1)


def main():
    testcases = [
        [1, 4, 3, 5, 6, 3, 4, 8],
        [5, 4, 6, 3, 2, 3, 6, 7],
        [9, 4, 3, 2, 6, 3, 7, 1],
        [3, 2, 1, 4, 5, 3, 2, 0],
        [8, 5, 4, 6, 3, 2, 9, 1]
    ]
    for tc in testcases:
        bst = BST()
        for i in tc:
            bst.insert(i)
        bst.print_tree()
        print()


if __name__ == "__main__":
    main()
