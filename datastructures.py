'''
数据结构
'''
'''
list 性能分析
'''
from timeit import Timer
def test1():
    l = []
    for i in range(1000):
        l = l+[i]
def test2():
    l = []
    for i in range(1000):
        l.append(i)
def test3():
    l = [i for i in range(1000)]
def test4():
    l = list(range(1000))

print("list-----")
t1 = Timer("test1()","from __main__ import test1")
print("contact ",t1.timeit(number=1000),'milliseconds')
t2 = Timer("test2()","from __main__ import test2")
print("append ",t2.timeit(number=1000),"milliseconds")
t3 = Timer("test3()","from __main__ import test3")
print("comprehension ",t3.timeit(number=1000),"milliseconds")
t4 = Timer("test4()","from __main__ import test4")
print("list range ",t4.timeit(number=1000),"milliseconds")

x = list(range(2000000))
pop_zero = Timer("x.pop(0)","from __main__ import x")
print("pop_zero ",pop_zero.timeit(number=1000),"milliseconds")
pop_end = Timer("x.pop()","from __main__ import x")
print("pop_end ",pop_end.timeit(number=1000),"milliseconds")

'''
Dictionary
'''
'''
import timeit
for i in range(10000,1000001,20000):
    t = timeit.Timer("random.randrange(%d) in x"%i,"from __main__ import random,x")
    x = list(range(i))
    lst_time = t.timeit(number=1000)
    x = {j:None for j in range(i)}
    d_time = t.timeit(number=1000)
    print("%d,%10.3f,%10.3f" % (i, lst_time, d_time))
'''

'''
栈 LIFO 先进先出
'''
class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items) - 1]
    def size(self):
        return len(self.items)

print("stack-----")
s = Stack()
print(s.is_empty())
s.push(4)
s.push("dog")
print(s.peek())
s.push(True)
print(s.size())
print(s.is_empty())
s.push(8.4)
print(s.pop())
print(s.pop())
print(s.size())

'''
队列：FIFO结构，先进先出
'''
class Queue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)

print("queue-----")
q = Queue()
q.enqueue('hello')
q.enqueue('dog')
print(q.items)
q.enqueue(3)
q.dequeue()
print(q.items)

'''
双向队列：左右两边都可以插入和删除的队列
'''
class Deque:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def add_front(self,item):
        self.items.append(item)
    def add_rear(self,item):
        self.items.insert(0,item)
    def remove_front(self):
        return self.items.pop()
    def remove_rear(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)

print("deque-----")
dq = Deque()
dq.add_front("dog")
dq.add_rear("cat")
print(dq.items)
dq.remove_front()
dq.add_front("pig")
print(dq.items)

'''
二叉树：一个节点最多有两个孩子节点的树。
如果是从0索引开始存储，那么对应于节点p的孩子节点是2p+1和2p+2两个节点，
相反，节点p的父亲节点是(p-1)/2位置上的点

二叉树的三种遍历方法(前序，中序，后序)
'''
'''
直接使用list来实现二叉树，可读性差
'''
def binary_tree(r):
    return [r,[],[]]
def insert_left(root,new_branch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1,[new_branch,t,[]])
    else:
        root.insert(1,[new_branch,[],[]])
    return root
def insert_right(root,new_branch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2,[new_branch,[],t])
    else:
        root.insert(2,[new_branch,[],[]])
    return root
def get_root_val(root):
    return root[0]
def set_root_val(root,new_val):
    root[0] = new_val
def get_left_child(root):
    return root[1]
def get_right_child(root):
    return root[2]


print("binary_tree-----")
r = binary_tree(3)
insert_left(r, 4)
insert_left(r, 5)
insert_right(r, 6)
insert_right(r, 7)
print(r)
l = get_left_child(r)
print(l)
set_root_val(l, 9)
print(r)
insert_left(l, 11)
print(r)
print(get_right_child(get_right_child(r)))

'''
使用类的形式定义二叉树，可读性更好
'''
class BinaryTree:
    def __init__(self,root):
        self.key = root
        self.left_child = None
        self.right_child = None
    def insert_left(self,new_node):
        if self.left_child == None:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self, new_node):
        if self.right_child == None:
            self.right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t
    def get_right_child(self):
        return self.right_child
    def get_left_child(self):
        return self.left_child
    def set_root_val(self,obj):
        self.key = obj
    def get_root_val(self):
        return self.key

print("binary-tree-----")
r = BinaryTree('a')
print(r.get_root_val())
print(r.get_left_child())
r.insert_left('b')
print(r.get_left_child())
print(r.get_left_child().get_root_val())
r.insert_right('c')
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val('hello')
print(r.get_right_child().get_root_val())

'''
二叉堆：根据堆的性质又可以分为最小堆和最大堆，是一种非常好的优先队列。
在最小堆中孩子节点一定大于等于其父亲节点，最大堆反之。
二叉堆实际上是一棵完全二叉树，并且满足堆的性质。
对于插入和查找操作的时间复杂度度都是O(logn)。
'''
'''
最小生成树
'''
class BinHeap:
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0
    def perc_up(self,i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                self.heap_list[i],self.heap_list[i // 2] = self.heap_list[i // 2],self.heap_list[i]
            i = i // 2
    def insert(self,k):
        self.heap_list.append(k)
        self.current_size = self.current_size + 1
        self.perc_up(self.current_size)
    def perc_down(self,i):
        while (i * 2) <= self.current_size:
            mc = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                self.heap_list[mc],self.heap_list[i] = self.heap_list[i],self.heap_list[mc]
            i = mc

    def min_child(self,i):
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1
    def del_min(self):
        ret_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size = self.current_size - 1
        self.heap_list.pop()
        self.perc_down(1)
        return ret_val

    def build_heap(self,a_list):
        i = len(a_list) // 2
        self.current_size = len(a_list)
        self.heap_list = [0] + a_list[:]  # append original list
        while (i > 0):
            # build the heap we only need to deal the first part!
            self.perc_down(i)
            i = i - 1
print("binheap-----")
a_list=[4,1,3,2,16,9,10,14,8,7];
bh=BinHeap();
bh.build_heap(a_list);
print(bh.heap_list)
print(bh.current_size)
bh.insert(10)
bh.insert(7)
print(bh.heap_list)
bh.del_min();
print(bh.heap_list)
print(bh.current_size)