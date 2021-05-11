class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def convertBST(root: TreeNode) -> TreeNode:
    runner = []
    stack = []

    curr = root
    while curr or runner:

        if curr:
            runner.append(curr)
            curr = curr.left

        elif runner:
            curr = runner.pop()
            stack.append(curr)

            curr = curr.right

    summ = 0
    while stack:
        node = stack.pop()

        summ += node.val
        node.val = summ

    return root
