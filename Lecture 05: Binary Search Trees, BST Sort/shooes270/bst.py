class Node:

    def __init__(self, data):
        self.parent = None
        self.left = None
        self.right = None
        self.data = data



class BST:

    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
            return
        self.__insert_node(self.root, data)

    def __insert_node(self, current_node, data):
        if not current_node:
            current_node = Node(data)
            return

        if current_node.data >= data:
            if current_node.left:
                self.__insert_node(current_node.left, data)
            else:
                current_node.left = Node(data)
                current_node.left.parent = current_node
        else:
            if current_node.right:
                self.__insert_node(current_node.right, data)
            else:
                current_node.right = Node(data)
                current_node.right.parent = current_node

    def find(self, data):
        if not self.root:
            return False
        return self.__find_node(self.root, data)

    def __find_node(self, current_node, data):
        if current_node.data == data:
            return True
        if current_node.data >= data and current_node.left:
            return self.__find_node(current_node.left, data)
        if current_node.data < data and current_node.right:
            return self.__find_node(current_node.right, data)
        return False

    def echo(self, node=None):
        """
        inorder방식으로 출력하여 정렬된 값들을 보여줌
        """
        if not self.root:
            return
        if not node:
            node = self.root
        if node.left:
            self.echo(node.left)
        print (node.data, end=' ')
        if node.right:
            self.echo(node.right)


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
        bst.echo()
        print( bst.find(4), bst.find(100))


if __name__ == "__main__":
    main()
