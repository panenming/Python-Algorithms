#伪代码
def divide_and_conquer(S,divide,combine):
    if len(S) == 1:
        return S
    L,R = divide(S)
    A = divide_and_conquer(L,divide,combine)
    B = divide_and_conquer(R,divide,combine)
    return combine(A,B)

print("python中分治算法的应用-----")
from bisect import bisect
a = [0, 2, 3, 5, 6, 7, 8, 8, 9]
print(bisect(a,5))
from bisect import bisect_left,bisect_right
print(bisect_left(a,5))
print(bisect_right(a,5))

'''
比较：二分法，二叉搜索树，字典

三者都是用来提高搜索效率的，但是各有区别。
二分法只能作用于有序数组(例如排序后的Python的list)，但是有序数组较难维护，因为插入需要线性时间；
二叉搜索树有些复杂，动态变化着，但是插入和删除效率高了些；
字典的效率相比而言就比较好了，插入删除操作的平均时间都是常数的，只不过它还需要计算下hash值才能确定元素的位置。
'''

'''
顺序统计量
在算法导论中一组序列中的第 k 大的元素定义为顺序统计量
'''
def partition(seq):
    pi,seq = seq[0],seq[1:]
    lo = [x for x in seq if x <= pi]
    hi = [x for x in seq if x > pi]
    return lo,pi,hi

def select(seq,k):
    lo,pi,hi = partition(seq)
    m = len(lo)
    if m == k:
        return pi
    elif m < k:
        return select(hi,k-m-1)
    else:
        return select(lo,k)

print("顺序统计量-----")
seq = [3, 4, 1, 6, 3, 7, 9, 13, 93, 0, 100, 1, 2, 2, 3, 3, 2]
print(partition(seq))
print(select([5, 3, 2, 7, 1], 3))
print(select([5, 3, 2, 7, 1], 4))
ans = [select(seq,k) for k in range(len(seq))]
seq.sort()
print(ans == seq)

def quicksort(seq):
    if len(seq) <= 1:
        return seq
    lo,pi,hi = partition(seq)
    return quicksort(lo) + [pi] + quicksort(hi)

print("快排算法-----")
seq = [7, 5, 0, 6, 3, 4, 1, 9, 8, 2]
print(quicksort(seq))

def mergesort(seq):
    mid = len(seq) // 2
    lft,rgt = seq[:mid],seq[mid:]
    if len(lft) > 1:
        lft = mergesort(lft)
    if len(rgt) > 1:
        rgt = mergesort(rgt)
    res = []
    while lft and rgt:
        if lft[-1] >= rgt[-1]:
            res.append(lft.pop())
        else:
            res.append(rgt.pop())
    res.reverse()
    return (lft or rgt) + res

print("合并排序算法-----")
seq = [7, 5, 0, 6, 3, 4, 1, 9, 8, 2]
print(mergesort(seq))