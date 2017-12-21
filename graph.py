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

'''
Bellman-Ford算法的一个重要作用：判断图中是否存在负权回路。
'''
#relaxtion
inf = float('inf')
def relax(W, u, v, D, P):
    d = D.get(u,inf) + W[u][v]                  # Possible shortcut estimate
    if d < D.get(v,inf):                        # Is it really a shortcut?
        D[v], P[v] = d, u                       # Update estimate and parent
        return True
#Bellman-Ford算法
def bellman_ford(G, s):
    D, P = {s:0}, {}                            # Zero-dist to s; no parents
    for rnd in G:                               # n = len(G) rounds
        changed = False                         # No changes in round so far
        for u in G:                             # For every from-node...
            for v in G[u]:                      # ... and its to-nodes...
                if relax(G, u, v, D, P):        # Shortcut to v from u?
                    changed = True              # Yes! So something changed
        if not changed: break                   # No change in round: Done
    else:                                       # Not done before round n?
        raise ValueError('negative cycle')      # Negative cycle detected
    return D, P                                 # Otherwise: D and P correct

#测试代码
s, t, x, y, z = range(5)
W = {
    s: {t:6, y:7},
    t: {x:5, y:8, z:-4},
    x: {t:-2},
    y: {x:-3, z:9},
    z: {s:2, x:7}
    }
D, P = bellman_ford(W, s)
print([D[v] for v in [s, t, x, y, z]]) # [0, 2, 4, 7, -2]
print(s not in P) # True
print([P[v] for v in [t, x, y, z]] == [x, y, s, t]) # True
W[s][t] = -100
print(bellman_ford(W, s))

#Dijkstra算法
from heapq import heappush, heappop

def dijkstra(G, s):
    D, P, Q, S = {s:0}, {}, [(0,s)], set()      # Est., tree, queue, visited
    while Q:                                    # Still unprocessed nodes?
        _, u = heappop(Q)                       # Node with lowest estimate
        if u in S: continue                     # Already visited? Skip it
        S.add(u)                                # We've visited it now
        for v in G[u]:                          # Go through all its neighbors
            relax(G, u, v, D, P)                # Relax the out-edge
            heappush(Q, (D[v], v))              # Add to queue, w/est. as pri
    return D, P                                 # Final D and P returned

#测试代码
s, t, x, y, z = range(5)
W = {
    s: {t:10, y:5},
    t: {x:1, y:2},
    x: {z:4},
    y: {t:3, x:9, z:2},
    z: {x:6, s:7}
    }
D, P = dijkstra(W, s)
print([D[v] for v in [s, t, x, y, z]]) # [0, 8, 9, 5, 7]
print(s not in P) # True
print([P[v] for v in [t, x, y, z]] == [y, t, s, y])# True
