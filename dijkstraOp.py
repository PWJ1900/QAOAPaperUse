import random
import networkx as nx

"""
作者： 潘文杰
"""
qubits = 5

def useGF():
    arr = []
    resultList = random.sample(range(0, qubits), qubits)
    #假设每两个点之间的概率为0.5
    for i in range(qubits):
        for j in range(i+1, qubits):
            if random.randint(1, 10) <= 5:
                arr.append((resultList[i], resultList[j]))
    G = nx.Graph()
    G.add_nodes_from(resultList)
    G.add_edges_from(arr)
    nx.draw(G, with_labels=True, alpha=0.8, node_size=500)
    print(resultList)
    print(arr)
    return arr

# 寻径算法设计（无权无向）
    ## 1、遇到非连通图的特殊场景怎么办（预先筛选出几个子图）
    ## 2、路径当将要形成环或者没有点时，停止查找
    ## 3、选出每个子图的最长路径

# 狄杰斯特拉：


# 获取最大值
def getMax(valueArrUse):
    abc = valueArrUse
    lenUse = len(abc)
    print(lenUse)
    temp = abc[0]
    for i in range(lenUse):
        if i < lenUse - 1 and temp[1] < abc[i+1][1]:
            temp = abc[i+1]
    print(temp)
    return temp

def useN(valueUse):
    lenUse = qubits
    for i in range(lenUse):
        if Remain[i] == valueUse:
            Remain[i] = [-1, -10000]


# edgesMid = [[5, 0], [4, 8], [6, 0], [6, 7], [6, 3], [0, 9], [0, 2], [1, 9], [1, 2], [8, 3]]
edgesMid = useGF() #初始化图
edges = []
for i in edgesMid:
    edges.append([i[0], i[1]])

print(edges)
arr = [([0] * qubits) for i in range(qubits)]
for i in range(qubits):
    for j in range(qubits):
        if [i, j] in edges or [j, i] in edges:
            arr[i][j] = 1
        else:
            arr[i][j] = 0
            arr[j][i] = 0
for i in range(qubits):
        print(arr[i])

v = [[i]for i in range(qubits)]
# 设置数组S为 [[v,dis]]
# 设置数组Remain为 [[v,dis]]
S = []
Remain = []
# 1、 先找0点出发
# S.append(0)
# for i in range(10):
#     if arr[0][i] != 0:
#         Remain.append([i, 1])


# 开始构造多点
# S.append([0, 0])
for i in range(qubits):
    Remain.append([i, 0])

for i in range(qubits):
    # S.append(Max(Remain[][1]所有的Remain里取distance的最大值放入S，作为下一个节点)) # 这个里面要注意以下每次都取dis最大值
    # Remain.remove("最小值")
    reduceV = getMax(Remain)
    S.append(reduceV)
    # Remain.remove(reduceV)
    useN(reduceV)
    for j in range(qubits):
        if arr[reduceV[0]][j] != 0 and Remain[j][0] > 0: # reudceV[0]为重新开始的节点  避免已经入了S集合的点重复找Remain[j][0] > 0
            Remain[j][1] = S[i][1] + 1

# 正好可以利用狄杰斯特拉变体的距离值去判断是否为分支
# 如果距离值为分支则就为数组中路径值w变小或者相等，并且S中与此顶点之前路径比其小的节点的下一个分支点
# 处理

def searchLess(valueArrUse, index):
    temp = 0
    for i in range(index):
        if S[i][1] < valueArrUse[1]:
            temp = S[i][0]
    return temp # 0坐标为顶点


edgeOp = []
step = 0
for i in range(len(S)):#判断数组第二权值为0便为两个图，做step判断
    if i >= 1:
        if S[i][1] == 0:
            continue
        if S[i-1][1] < S[i][1]:
            edgeOp.append([S[i-1][0], S[i][0]])
        else:
            edgeOp.append([searchLess(S[i], i), S[i][0]])

print(edgeOp)
print(S)



# getMax([[1, 2], [3, 8], [5, 6]])

# print(S)
# print(Remain)
#
# # for i in range(10):
# #     for j in range(10):
# #         if
#
# print(v)





