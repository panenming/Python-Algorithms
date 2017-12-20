'''
贪心算法顾名思义就是每次都贪心地选择当前最好的那个(局部最优解)，不去考虑以后的情况，而且选择了就不能够“反悔”了，
如果原问题满足贪心选择性质和最优子结构，那么最后得到的解就是最优解。
贪心算法和其他的算法比较有明显的区别，动态规划每次都是综合所有子问题的解得到当前的最优解(全局最优解)，而不是贪心地选择；
回溯法是尝试选择一条路，如果选择错了的话可以“反悔”，也就是回过头来重新选择其他的试试。
'''
'''
哈夫曼编码
'''
from heapq import heapify,heappush,heappop
from itertools import count

def huffman(seq,frq):
    num = count()
    trees = list(zip(frq,num,seq))
    while len(trees) > 1:
        fa,_,a = heappop(trees)
        fb,_,b = heappop(trees)
        n = next(num)
        heappush(trees,(fa+fb,n,[a,b]))
    return trees[0][-1]

print("huffman-----")
seq = "abcdefghi"
frq = [4, 5, 6, 9, 11, 12, 15, 16, 20]
print(huffman(seq,frq))

'''
最小生成树
Kruskal和Prim算法，两个算法都是基于贪心策略
'''
def naive_find(C,u):
    while C[u] != u:
        u = C[u]
    return u

def naive_union(C, u, v):
    u = naive_find(C, u)                        # Find both reps
    v = naive_find(C, v)
    C[u] = v                                    # Make one refer to the other

def naive_kruskal(G):
    E = [(G[u][v],u,v) for u in G for v in G[u]]
    T = set()                                   # Empty partial solution
    C = {u:u for u in G}                        # Component reps
    for _, u, v in sorted(E):                   # Edges, sorted by weight
        if naive_find(C, u) != naive_find(C, v):
            T.add((u, v))                       # Different reps? Use it!
            naive_union(C, u, v)                # Combine components
    return T

#Kruskal’s Algorithm
def find(C, u):
    if C[u] != u:
        C[u] = find(C, C[u])                    # Path compression
    return C[u]

def union(C, R, u, v):
    u, v = find(C, u), find(C, v)
    if R[u] > R[v]:                             # Union by rank
        C[v] = u
    else:
        C[u] = v
    if R[u] == R[v]:                            # A tie: Move v up a level
        R[v] += 1

def kruskal(G):
    E = [(G[u][v],u,v) for u in G for v in G[u]]
    T = set()
    C, R = {u:u for u in G}, {u:0 for u in G}   # Comp. reps and ranks
    for _, u, v in sorted(E):
        if find(C, u) != find(C, v):
            T.add((u, v))
            union(C, R, u, v)
    return T

def prim(G,s):
    P,Q = {},[(0,None,s)]
    while Q:
        _,p,u = heappop(Q)
        if u in P:
            continue
        P[u] = p
        for v,w in G[u].items():
            heappush(Q,(w,u,v))
    return P

print("最小生成树kruskal----")
G = {
    0: {1:1, 2:3, 3:4},
    1: {2:5},
    2: {3:2},
    3: set()
    }
print(list(naive_kruskal(G)))


print("最小生成树prim----")
G = {
    0: {1:1, 2:3, 3:4},
    1: {0:1, 2:5},
    2: {0:3, 1:5, 3:2},
    3: {2:2, 0:4}
    }
print(prim(G, 0))

'''
Greed Works. But When?
算法导论中还介绍了贪心算法的内在原理，也就是拟阵，贪心算法一般都是求这个拟阵的最大独立子集，方法就是从一个空的独立子集开始，
从一个已经经过排序的序列中依次取出一个元素，尝试添加到独立子集中，如果新元素加入之后的集合仍然是一个独立子集的话那就加入进去，
这样就形成了一个更大的独立子集，待遍历完整个序列时我们就得到最大的独立子集。
'''