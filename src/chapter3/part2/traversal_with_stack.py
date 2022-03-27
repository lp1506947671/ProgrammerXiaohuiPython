# 二叉树
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# 构建二叉树
def create_binary_tree(input_list):
    if not input_list:
        return None
    data = input_list.pop(0)
    if data is None:
        return None
    node = TreeNode(data)
    node.left = create_binary_tree(input_list)
    node.right = create_binary_tree(input_list)
    return node


# 前序遍历
# https://leetcode-cn.com/problems/binary-tree-preorder-traversal/solution/er-cha-shu-de-qian-xu-bian-li-by-leetcode-solution/
def pre_order_traversal_with_stack(root):
    if not root:
        return []
    stack, res = [], []
    while root or stack:
        while root:
            res.append(root.data)
            stack.append(root)
            root = root.left
        root = stack.pop()
        root = root.right
    return res


# 中序遍历
# https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/jian-dan-yi-dong-javac-pythonjs-er-cha-s-w80i/
def in_order_traversal_with_stack(root):
    if not root:
        return []
    stack, res = [], []
    while root or stack:
        while root:
            # 左节点
            stack.append(root)
            root = root.left
        # 没有左节点
        root = stack.pop()
        res.append(root.data)
        root = root.right

    return res


# 后续遍历
# https://leetcode-cn.com/problems/binary-tree-postorder-traversal/solution/er-cha-shu-de-hou-xu-bian-li-by-leetcode-solution/
def post_order_traversal_with_stack(root):
    if not root:
        return []
    stack, res = [], []
    prev = None
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        if not root.right or root.right == prev:
            res.append(root.data)
            prev = root
            root = None
        else:
            stack.append(root)
            root = root.right
    return res


if __name__ == '__main__':
    my_input_list = [3, 9, None, None, 4, 5, None, None, 7, None, None]
    root1 = create_binary_tree(my_input_list)
    print("前序遍历：")
    print("result", [3, 9, 4, 5, 7])
    print("current", pre_order_traversal_with_stack(root1))
    # print("中序遍历：")
    # print("result", [9, 7, 5, 4, 3])
    # print("current", in_order_traversal_with_stack(root1))
    # print("后序遍历：")
    # print("result", [9, 5, 7, 4, 3])
    # print("current", post_order_traversal_with_stack(root1))
