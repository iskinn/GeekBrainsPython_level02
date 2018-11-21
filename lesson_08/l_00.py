from binarytree import tree, bst, Node

a = tree(height=3, is_perfect=False)
b = bst(height=3, is_perfect=True)
c = Node(5)
c.left = Node(3)
c.right = Node(10)
c.left.left = Node(2)
c.left.right = Node(4)
c.right.left = Node(9)
c.right.right = Node(15)


#print(a)
#print(b)
#print(c)

bt = bst(height=5, is_perfect=True)
print(bt)

num = int(input('Что найти: '))

def search(bin_tree, number, path=''):
    if bin_tree.value == number:
        return f'Число {number} обнаружено по следующему пути: \nКорень{path}'
    if number < bin_tree.value and bin_tree.left != None:
        return search(bin_tree.left, number, path=f'{path}\nШаг влево')
    if number > bin_tree.value and bin_tree.right != None:
        return search(bin_tree.right, number, path=f'{path}\nШаг вправо')
    return f'Число {number} отсутствует'

print(search(bt, num))
