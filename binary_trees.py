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

    def bfs(self, node):

        visited = []
        tracker = []
        tracker.append(node)
        while len(tracker) > 0:
            node = tracker.pop(0)
            if node:
                visited.append(node.data)
                tracker.append(node.left)
                tracker.append(node.right)
        print(visited)

def main():
    t = Tree()
    t.add(15)
    t.add(19)
    t.add(4)
    t.add(12)
    t.add(18)
    t.add(21)
    print("Pre-Order Traversal: ")
    t.print_pre_order(t.root)
    print()
    print("In-Order Traversal: ")
    t.print_in_order(t.root)
    print()
    print("Post-Order Traversal: ")
    t.print_post_order(t.root)
    print()
    print("By Level Traversal: ")
    t.bfs(t.root)
    print()


if __name__ == "__main__":
    main()
