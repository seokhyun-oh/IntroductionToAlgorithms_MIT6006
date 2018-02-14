from bst import BST


def height(node):
    if node is None:
        return -1
    return node.height


def update_height(node):
    node.height = max(height(node.left), height(node.right)) + 1


class AVL(BST):

    def __init__(self):
        BST.__init__(self)

    def __rotate_left(self, node):
        right = node.right
        right.parent = node.parent
        if right.parent is None:
            self.root = right
        else:
            if right.parent.left is node:
                right.parent.left = right
            elif right.parent.right is node:
                right.parent.right = right
        node.right = right.left
        if node.right is not None:
            node.right.parent = node
        right.left = node
        node.parent = right
        update_height(node)
        update_height(right)

    def __rotate_right(self, node):
        left = node.left
        left.parent = node.parent
        if left.parent is None:
            self.root = left
        else:
            if left.parent.left is node:
                left.parent.left = left
            elif left.parent.right is node:
                left.parent.right = left
        node.left = left.right
        if node.left is not None:
            node.left.parent = node
        left.right = node
        node.parent = left
        update_height(node)
        update_height(left)

    def __rebalance(self, node):
        if node is None:
            return
        update_height(node)
        if height(node.left) - height(node.right) == 2:
            child = node.left
            if height(child.left) > height(child.right):
                self.__rotate_right(node)
            else:
                self.__rotate_left(child)
                self.__rotate_right(node)
        elif height(node.right) - height(node.left) == 2:
            child = node.right
            if height(child.left) > height(child.right):
                self.__rotate_right(child)
                self.__rotate_left(node)
            else:
                self.__rotate_left(node)
        self.__rebalance(node.parent)

    def insert(self, key):
        node = BST.insert(self, key)
        self.__rebalance(node)


def main():
    testcases = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [9, 8, 7, 6, 5, 4, 3, 2, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
        [9, 4, 3, 2, 6, 3, 7, 1],
        [3, 2, 1, 4, 5, 3, 2, 0],
        [8, 5, 4, 6, 3, 2, 9, 1]
    ]
    for tc in testcases:
        print("test : ", tc)
        bst, avl = BST(), AVL()
        for i in tc:
            bst.insert(i)
            avl.insert(i)
        print("binary search tree")
        bst.print_tree()
        print("AVL tree")
        avl.print_tree()
        print()


if __name__ == "__main__":
    main()
