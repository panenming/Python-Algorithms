'''
动态规划算法一般都有下面两种实现方式
备忘录法和迭代法

1.直接自顶向下实现递归式，并将中间结果保存，这叫备忘录法；

2.按照递归式自底向上地迭代，将结果保存在某个数据结构中求解。
'''
from functools import wraps
def memo(func):
    cache = {}
    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap

@memo
def fib(i):
    if i < 2:
        return 1
    return fib(i - 1) + fib(i - 2)

print(fib(100))

'''
带备忘录的递归方式的优点就是易于理解，易于实现，代码简洁干净，运行速度也不错，直接从需要求解的问题出发，而且只计算需要求解的子问题，没有多余的计算。
但是，它也有自己的缺点，因为是递归形式，所以有限的栈深度是它的硬伤，有些问题难免会出现栈溢出了。

迭代实现方式有2个好处：
1.运行速度快，因为没有用栈去实现，也避免了栈溢出的情况；
2.迭代实现的话可以不使用dict来进行缓存，而是使用其他的特殊cache结构，例如多维数组等更为高效的数据结构。

递归实现不需要去考虑计算顺序，只要给出问题，然后自顶向下去解就行；
而迭代实现需要考虑计算顺序，并且顺序很重要，算法在运行的过程中要保证当前要计算的问题中的子问题的解已经是求解好了的。
'''

def fib_iter(n):
    if n < 2:
        return 1
    a ,b = 1,1
    while n >= 2:
        c = a + b
        a = b
        b = c
        n = n - 1
    return c

print(fib_iter(1000))

'''
求二项式系数的递归实现
'''
@memo
def cnk(n,k):
    if k==0: return 1 #the order of `if` should not change!!!
    if n==0: return 0
    return cnk(n-1,k)+cnk(n-1,k-1)

'''
迭代版本
'''
from collections import defaultdict
n,k = 10,7
C = defaultdict(int)
for row in range(n + 1):
    C[row,0] = 1
    for col in range(1,k+1):
        C[row,col] = C[row-1,col-1] + C[row - 1,col]
print(C[n,k])

'''
用动态规划解决有向无环图的单源最短路径
去哪里?
我们顺向思维，首先假设从a点出发到所有其他点的距离都是无穷大，然后，按照拓扑排序的顺序，
从a点出发，接着更新a点能够到达的其他的点的距离，那么就是b点和f点，b点的距离变成2，f点的距离变成9。因为这个有向无环图是经过了拓扑排序的，
所以按照拓扑顺序访问一遍所有的点(到了目标点就可以停止了)就能够得到a点到所有已访问到的点的最短距离，
也就是说，当到达哪个点的时候，我们就找到了从a点到该点的最短距离，拓扑排序保证了后面的点不会指向前面的点，
所以访问到后面的点时不可能再更新它前面的点的最短距离！这种思维方式的代码实现就是迭代版本。
'''
def topsort(W):
    return W

def dag_sp(W, s, t):
    d = {u:float('inf') for u in W} #
    d[s] = 0
    for u in topsort(W):
        if u == t: break
        for v in W[u]:
            d[v] = min(d[v], d[u] + W[u][v])
    return d[t]

#邻接表
W={0:{1:2,5:9},1:{2:1,3:2,5:6},2:{3:7},3:{4:2,5:3},4:{5:4},5:{}}
s,t=0,5
print(dag_sp(W,s,t)) #7

'''
“从哪里来?“：我们逆向思维，目标是要到f，那从a点经过哪个点到f点会近些呢?只能是求解从a点出发能够到达的那些点哪个距离f点更近，
这里a点能够到达b点和f点，f点到f点距离是0，但是a到f点的距离是9，可能不是最近的路，所以还要看b点到f点有多近，
看b点到f点有多近就是求解从b点出发能够到达的那些点哪个距离f点更近，所以又绕回来了，也就是递归下去，
直到我们能够回答从a点经过哪个点到f点会更近。这种思维方式的代码实现就是递归版本。
'''

def rec_dag_sp(W,s,t):
    @memo
    def d(u):
        if u == t :
            return 0
        return min(W[u][v] + d(v) for v in W[u])
    return d(s)

#邻接表
W={0:{1:2,5:9},1:{2:1,3:2,5:6},2:{3:7},3:{4:2,5:3},4:{5:4},5:{}}
s,t=0,5
print(rec_dag_sp(W,s,t))

'''
动态规划其实就是一个连续决策的过程，
每次决策我们可能有多种选择(二项式系数和0-1背包问题中我们只有两个选择，DAG图的单源最短路径中我们的选择要看点的出边或者入边，矩阵链乘问题中就是矩阵链可以分开的位置总数…)，
我们每次选择最好的那个作为我们的决策。所以，动态规划的时间复杂度其实和这两者有关，也就是子问题的个数以及子问题的选择个数，一般情况下动态规划算法的时间复杂度就是两者的乘积。

动态规划有两种实现方式：一种是带备忘录的递归形式，这种方式直接从原问题出发，遇到子问题就去求解子问题并存储子问题的解，
下次遇到的时候直接取出来，问题求解的过程看起来就像是先自顶向下地展开问题，然后自下而上的进行决策；
另一个实现方式是迭代方式，这种方式需要考虑如何给定一个子问题的求解方式，使得后面求解规模较大的问题是需要求解的子问题都已经求解好了，
它的缺点就是可能有些子问题不要算但是它还是算了，而递归实现方式只会计算它需要求解的子问题。
'''

'''
最长公共子序列(LCS)是典型的动态规划问题
LCS的五种实现：分别为0：直接递归；1：带备忘录的递归；2：使用二维数组保存结果的迭代；3：使用2个一维数组保存结果的迭代；4：使用1个一维数组和额外的O(1)空间保存结果的迭代。
'''
x,y='abcde','oaob'
def lcs0(i,j):
    if i < 0 or j < 0 :
        return 0
    if x[i] == y[j]:
        return lcs0(i - 1,j - 1) + 1
    return max(lcs0(i - 1,j),lcs0(i,j - 1))
print("lcs0-----")
lenx,leny = len(x),len(y)
print(lcs0(lenx-1,leny -1))

@memo
def lcs1(i,j):
    if i < 0 or j < 0:
        return 0
    if x[i] == y[j]:
        return lcs1(i - 1,j - 1) + 1
    return max(lcs1(i - 1,j),lcs1(i,j - 1))
print("lcs1-----")
print(lcs1(lenx - 1,leny - 1))

def lcs2(x,y):
    lenx,leny = len(x),len(y)
    minlen,maxlen = 0,0
    if lenx < leny:
        minlen,maxlen = lenx,leny
        x,y=y,x
    else:
        minlen,maxlen = leny,lenx
    s = [[0 for j in range(minlen)] for i in range(maxlen)]
    for i in range(maxlen):
        for j in range(minlen):
            if x[i] == y[j]:
                s[i][j] = s[i - 1][j - 1] + 1
            else:
                s[i][j] = max(s[i - 1][j],s[i][j - 1])
    return s
print("lcs2-----")
print(lcs2(x,y))

def lcs3(x,y):
    lenx,leny=len(x),len(y)
    minlen,maxlen=0,0
    if lenx<leny: minlen,maxlen=lenx,leny; x,y=y,x
    else: minlen,maxlen=leny,lenx;
    #s is maxlen * minlen
    pre=[0 for j in range(minlen)]
    cur=[0 for j in range(minlen)]
    for i in range(maxlen): #so, let x be the longer string!!!
        for j in range(minlen):
            if x[i]==y[j]: cur[j]=pre[j-1]+1
            else: cur[j]=max(pre[j],cur[j-1])
        pre[:]=cur[:]
    return cur

print("lcs3-----")
print(lcs3(x,y))

def lcs4(x,y):
    lenx,leny = len(x),len(y)
    minlen,maxlen = 0,0
    if lenx < leny:
        minlen,maxlen = lenx,leny
        x,y = y,x
    else:
        minlen,maxlen = leny,lenx
    s = [0 for j in range(minlen)]
    t = 0
    for i in range(maxlen):
        for j in range(minlen):
            if x[i] == y[j]:
                s[j] = t + 1
            else:
                s[j] = max(s[j],s[j - 1])
            t = s[j]
    return s

print("lcs4-----")
print(lcs4(x,y))
