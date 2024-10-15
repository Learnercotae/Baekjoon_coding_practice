class BinaryTree:
    def __init__(self):
        self.tree = {}

    def add_node(self, root, left, right):
        self.tree[root] = (left, right)

    def preorder(self, root):
        if root == '.':
            return ""
        left, right = self.tree[root]
        return root + self.preorder(left) + self.preorder(right)

    def inorder(self, root):
        if root == '.':
            return ""
        left, right = self.tree[root]
        return self.inorder(left) + root + self.inorder(right)

    def postorder(self, root):
        if root == '.':
            return ""
        left, right = self.tree[root]
        return self.postorder(left) + self.postorder(right) + root


n = int(input())  # 트리의 노드 개수
bt = BinaryTree()

# 트리 정보 입력
for _ in range(n):
    root, left, right = input().split()
    bt.add_node(root, left, right)

# 전위, 중위, 후위 순회 결과 출력
print(bt.preorder('A'))  # 루트가 'A'라고 가정
print(bt.inorder('A'))
print(bt.postorder('A'))