import sys
 
N = int(sys.stdin.readline().strip())
tree = {}
 
for n in range(N):
    root, left, right = sys.stdin.readline().strip().split()

    #트리 딕셔너리에 노드 정보 저장 ex)tree['A']=['B','C']
    tree[root] = [left, right]
 
 #전위 함수
def preorder(root):
    if root != '.':
        print(root, end='')  # root
        preorder(tree[root][0])  # left
        preorder(tree[root][1])  # right
 
 #중위 함수
def inorder(root):
    if root != '.':
        inorder(tree[root][0])  # left
        print(root, end='')  # root
        inorder(tree[root][1])  # right
 
 #후위 함수
def postorder(root):
    if root != '.':
        postorder(tree[root][0])  # left
        postorder(tree[root][1])  # right
        print(root, end='')  # root
 
 #트리를 순회하고 결과 출력
preorder('A') #전위 순회, 시작은 항상 'A'(루트)로 시작
print()
inorder('A')
print()
postorder('A')