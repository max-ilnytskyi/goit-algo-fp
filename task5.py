import heapq
import uuid
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.colors import to_hex, rgb_to_hsv, hsv_to_rgb
import numpy as np


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(
        tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors
    )
    plt.show()


def build_heap_tree(heap):
    if not heap:
        return None

    nodes = [Node(key) for key in heap]
    for i in range(len(nodes)):
        left_index = 2 * i + 1
        right_index = 2 * i + 2

        if left_index < len(nodes):
            nodes[i].left = nodes[left_index]
        if right_index < len(nodes):
            nodes[i].right = nodes[right_index]

    return nodes[0]


def color_gradient(n, base_color="#1296F0"):
    base_rgb = np.array([int(base_color[i:i+2], 16) for i in (1, 3, 5)]) / 255.0
    base_hsv = rgb_to_hsv(base_rgb)

    gradients = [hsv_to_rgb([base_hsv[0], base_hsv[1], 0.3 + (0.7 * i / n)]) for i in range(n)]
    return [to_hex(color) for color in gradients]


def dfs_visualize(root):
    if not root:
        return

    stack = [root]
    visited = []
    colors = color_gradient(len(get_nodes(root)))

    index = 0
    while stack:
        node = stack.pop()
        if node not in visited:
            node.color = colors[index]
            visited.append(node)
            index += 1

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    draw_tree(root)


def bfs_visualize(root):
    if not root:
        return

    queue = [root]
    visited = []
    colors = color_gradient(len(get_nodes(root)))

    index = 0
    while queue:
        node = queue.pop(0)
        if node not in visited:
            node.color = colors[index]
            visited.append(node)
            index += 1

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    draw_tree(root)


def get_nodes(root):
    nodes = []
    queue = [root]

    while queue:
        node = queue.pop(0)
        nodes.append(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return nodes


# Example heap
heap = [0, 4, 1, 5, 10, 3]

# Transform the list into a heap
heapq.heapify(heap)

# Build the binary tree from the heap
root = build_heap_tree(heap)

# Visualize DFS traversal
print("DFS Traversal:")
dfs_visualize(root)

# Reset colors for BFS
for node in get_nodes(root):
    node.color = "skyblue"

# Visualize BFS traversal
print("BFS Traversal:")
bfs_visualize(root)
