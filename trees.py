from collections import defaultdict

# Binary-Tree Node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


x = TreeNode(3); x.left = TreeNode(1); x.left.left = TreeNode(0); x.right = TreeNode(4)


def traverse_in_order(root):
    if root.left:
        yield from traverse_in_order(root.left)
    yield root.val
    if root.right:
        yield from traverse_in_order(root.right)
#print(*traverse_in_order(x))


def traverse_pre_order(root):
    yield root.val
    if root.left:
        yield from traverse_pre_order(root.left)
    if root.right:
        yield from traverse_pre_order(root.right)
#print(*traverse_pre_order(x))


def traverse_post_order(root):
    if root.left:
        yield from traverse_post_order(root.left)
    if root.right:
        yield from traverse_post_order(root.right)
    yield root.val
#print(*traverse_post_order(x))


def traverse_in_order_it(root):
    q = [root]
    while q:
        node = q.pop()
        if node:
            if type(node) is tuple:
                yield node[0]
            else:
                q.extend([node.right, (node.val,), node.left])
#print(*traverse_in_order_it(x))


def traverse_pre_order_it(root):
    q = [root]
    while q:
        node = q.pop()
        if node:
            yield node.val
            q.extend([node.right, node.left])
#print(*traverse_pre_order_it(x))


def traverse_post_order_it(root):
    q = [root]
    while q:
        node = q.pop()
        if node:
            if type(node) is tuple:
                yield node[0]
            else:
                q.extend([(node.val,), node.right, node.left])
#print(*traverse_post_order_it(x))


def leaves_values(root):
    if not root:
        return
    else:
        if not (root.left or root.right):
            yield root.val
        else:
            yield from leaves_values(root.left)
            yield from leaves_values(root.right)
#print(*leaves_values(x))


def tree_height(root):
    if not root:
        return 0
    else:
        return 1 + max(map(tree_height, (root.left, root.right)))
#print(tree_height(x))


def tree_layers_rel(root):
    layers = defaultdict(list)

    def traverse(root):
        if not root:
            return 0
        else:
            height = 1 + max(map(traverse, (root.left, root.right)))
            layers[height].append(root.val)
            return height

    traverse(root)
    return [(h + 1, layers[h + 1]) for h in range(len(layers))]
#print(*tree_layers_rel(x))


def tree_layers(root):
    layers = defaultdict(list)

    def traverse(root, h=0):
        if root:
            layers[h].append(root.val)
            [traverse(r, h + 1) for r in (root.left, root.right)]
        else:
            return

    traverse(root)

    return [(h + 1, layers[h]) for h in range(len(layers))]
#print(*tree_layers(x))


# aka invert
def reflect_tree(root):
    if root:
        root.left, root.right = map(reflect_tree, (root.right, root.left))
    return root
#print(*traverse_in_order(reflect_tree(x)))


def tree_equals(ta, tb):
    if (ta and not tb) or (tb and not ta):  # only one of them has children
        return False
    else:
        return not (ta or tb) or\
               (ta.val == tb.val and tree_equals(ta.left, tb.left) and tree_equals(ta.right, tb.right))
#print(tree_equals(x, x))


def _bst_balanced(root):
    if not root:
        return 1
    else:
        left, right = map(_bst_balanced, (root.left, root.right))
        return max(left, right) + 1 if all((left, right)) and abs(left - right) <= 1 else 0


def bst_balanced(root):
    return bool(_bst_balanced(root))

#x.left.left.left = TreeNode(5)
#print(bst_balanced(x))

