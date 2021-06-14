#!/usr/bin/env python3

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:

    def __init__(self):
        self.root = None

    def add(self, value):

        if self.root is None:
            self.root = Node(value)
            return

        node = self.root
        parent = None
        while node:
            parent = node
            if value < node.data:
                node = node.left
            else:
                node = node.right
        
        if value < parent.data:
            parent.left = Node(value)
        else:
            parent.right = Node(value)

    def print_pre_order(self, node):
        if node:
            print(node.data, end=" ")
            self.print_pre_order(node.left)
            self.print_pre_order(node.right)

    def print_in_order(self, node):
        if node:
            self.print_in_order(node.left)
            print(node.data, end=" ")
            self.print_in_order(node.right)

    def print_post_order(self, node):
        if node:
            self.print_post_order(node.left)
            self.print_post_order(node.right)
            print(node.data, end=" ")



def main():
    t = Tree()
    t.add(3)
    t.add(15)
    t.add(4)
    t.add(7)
    t.add(19)
    print("Pre-Order Traversal: ")
    t.print_pre_order(t.root)
    print()
    print("In-Order Traversal: ")
    t.print_in_order(t.root)
    print()
    print("Post-Order Traversal: ")
    t.print_post_order(t.root)
    print()


if __name__ == "__main__":
    main()
