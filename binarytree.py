'''class Node:
    def __init__(self,data):
        self.data=data
        self.r_child=None
        self.l_child=None
class Tree():
    def __init__(self):
        self.root=None
o=Tree()
n=Node(10)
n1=Node(20)
n2=Node(30)
n3=Node(40)
n4=Node(50)
n5=Node(60)
n6=Node(70)
o.root=n
n.r_child=n1
n.l_child=n2
n1.r_child=n3
n1.l_child=n4
n2.r_child=n5
n2.l_child=n6
print(o.root)
print(n)
print(n.r_child)
print(n1)
print(n.l_child)
print(n2)
print(n1.r_child)
print(n3)
print(n1.l_child)
print(n4)
print(n2.r_child)
print(n5)
print(n2.l_child)
print(n6)'''

print("__________________________________BST_____________________________________")
class Node:
    def __init__(self,data):
        self.data=data
        self.r_child=None
        self.l_child=None
class Tree():
    def __init__(self):
        self.root=None
o=Tree()
n=Node(10)
n1=Node(20)
n2=Node(30)
n3=Node(40)
n4=Node(50)
n5=Node(60)
n6=Node(70)
o.root=n3
n3.r_child=n5
n3.l_child=n1
n1.r_child=n2
n1.l_child=n
n5.r_child=n6
n5.l_child=n4
print(n1.r_child.data,n1.l_child.data,n3.l_child.data,o.root.data,n3.r_child.data,n5.r_child.data,n5.l_child.data,end=" ")




