'''
图的遍历
'''
def some_graph():
    a,b,c,d,e,f,g,h = range(8)
    N = [
        [b, c, d, e, f],  # a
        [c, e],  # b
        [d],  # c
        [e],  # d
        [f],  # e
        [c, g, h],  # f
        [f, h],  # g
        [f, g]  # h
    ]
    print(a,b,c,d,e,f,g,h)
    return N

def walk(G,s,S=set()):
    P,Q = dict(),set()
    P[s] = None
    Q.add(s)
    while Q:
        u = Q.pop()
        for v in G[u].difference(P, S):
            Q.add(v)
            P[v] = u
    return P

G = some_graph()
for i in range(len(G)):
    G[i] = set(G[i])
print(list(walk(G,0)))

'''
深度优先搜索(DFS)
'''
def rec_dfs(G,s,S=None):
    if S is None:
        S = set()
    S.add(s)
    for u in G[s]:
        if u in S:
            continue
        rec_dfs(G,u,S)
    return S
def iter_dfs(G,s):
    S,Q = set(),[]
    Q.append(s)
    while Q:
        u = Q.pop()
        if u in S:
            continue
        S.add(u)
        Q.extend(G[u])  # Schedule all neighbors
        yield u # Report u as visited
'''
通用遍历函数
'''
def traverse(G, s, qtype=set):
    S, Q = set(), qtype()
    Q.add(s)
    while Q:
        u = Q.pop()
        if u in S:
            continue
        S.add(u)
        for v in G[u]:
            Q.add(v)
        yield u
print("深度优先搜索-----")
G = some_graph()
for i in range(len(G)):
    G[i] = set(G[i])
print(list(rec_dfs(G,0)))
print(list(iter_dfs(G,0)))
class stack(list):
    add = list.append
print(list(traverse(G,0,stack)))
'''
加上时间戳的DFS
'''
#Depth-First Search with Timestamps
def dfs(G,s,d,f,S=None,t=0):
    if S is None:
        S = set()
    d[s] = t
    t = t + 1
    S.add(s)
    for u in G[s]:
        if u in S:
            continue
        t = dfs(G, u, d, f, S, t)
        f[s] = t
        t = t + 1
        return t

#Python的list可以很好地充当stack，但是充当queue则性能很差
#Breadth-First Search
from collections import deque
def bfs(G,s):
    P,Q = {s:None},deque([s])
    while Q:
        u = Q.popleft()
        for v in G[u]:
            if v in P:
                continue
            P[v] = u
            Q.append(v)
    return P

print("广度优先搜索-----")
G = some_graph()
print(bfs(G,0))

'''
强连通分支算法的流程有下面四步：

1.对原图G运行DFS，得到每个节点的完成时间f[v]；

2.得到原图的转置图GT；

3.对GT运行DFS，主循环按照节点的f[v]降序进行访问；

4.输出深度优先森林中的每棵树，也就是一个强连通分支。
'''
def tr(G):                                      # Transpose (rev. edges of) G
    GT = {}
    for u in G:
        GT[u] = set()                   # Get all the nodes in there
    for u in G:
        for v in G[u]:
            GT[v].add(u)                        # Add all reverse edges
    return GT

#Topological Sorting Based on Depth-First Search
def dfs_topsort(G):
    S, res = set(), []                          # History and result
    def recurse(u):                             # Traversal subroutine
        if u in S:
            return                       # Ignore visited nodes
        S.add(u)                                # Otherwise: Add to history
        for v in G[u]:
            recurse(v)                          # Recurse through neighbors
        res.append(u)                           # Finished with u: Append it
    for u in G:
        recurse(u)                              # Cover entire graph
    res.reverse()                               # It's all backward so far
    return res

def scc(G):
    GT = tr(G)                                  # Get the transposed graph
    sccs, seen = [], set()
    for u in dfs_topsort(G):                    # DFS starting points
        if u in seen:
            continue                  # Ignore covered nodes
        C = walk(GT, u, seen)                   # Don't go "backward" (seen)
        seen.update(C)                          # We've now seen C
        sccs.append(C)                          # Another SCC found
    return sccs

from string import ascii_lowercase
def parse_graph(s):
    # print zip(ascii_lowercase, s.split("/"))
    # [('a', 'bc'), ('b', 'die'), ('c', 'd'), ('d', 'ah'), ('e', 'f'), ('f', 'g'), ('g', 'eh'), ('h', 'i'), ('i', 'h')]
    G = {}
    for u, line in zip(ascii_lowercase, s.split("/")):
        G[u] = set(line)
    return G

print("强联通-----")
G = parse_graph('bc/die/d/ah/f/g/eh/i/h')
print(list(map(list, scc(G))))
