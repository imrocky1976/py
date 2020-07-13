"""
功能：图的邻接表实现
作者：shihj
日期：2020/06/03
"""

import sys
import queue

class VextexNode(object):
    """
    顶点节点
    """
    def __init__(self, value=None):
        self.value: any = value # 存储顶点信息
        self.first: EdgeNode = None # 边表的头指针

class EdgeNode(object):
    """
    边节点
    """
    def __init__(self, vextex, weight=0):
        self.vextex: int = vextex # 该边对应的顶点下标，从0开始
        self.weight: int = weight # 权值，非网图忽略
        self.next: EdgeNode = None # 下一个边

class AdjList(object):
    def __init__(self, directed=False, weighted=False):
        super(AdjList, self).__init__()
        self._vextexs: list(VextexNode) = []
        self._num_nodes: int = 0
        self._num_edges: int = 0
        self._directed: bool = directed # 是否有向图
        self._weighted: bool = weighted # 是否有权值

    def num_nodes(self):
        return self._num_nodes

    def num_edges(self):
        return self._num_edges
    
    def bfs_print(self):
        """
        广度优先遍历图，使用队列
        """
        visited = [False] * self._num_nodes
        queue_list = []
        for i in range(self._num_nodes):
            if not visited[i]: 
                queue_list.append(i)
                while queue_list:
                    node_index = queue_list.pop(0)
                    visited[node_index] = True
                    print('index: {}, node: {}'.format(node_index, self._vextexs[node_index].value))
                    edge = self._vextexs[node_index].first
                    while edge:
                        if self._weighted:
                            print('edge: {} - {}, weight: {}'.format(node_index, edge.vextex, edge.weight))
                        else:
                            print('edge: {} - {}'.format(node_index, edge.vextex))
                        if not visited[edge.vextex] and edge.vextex not in queue_list:
                            queue_list.append(edge.vextex)
                        edge = edge.next

    def dfs_print(self):
        """
        深度优先遍历图，使用栈
        """
        visited = [False] * self._num_nodes
        stack = []
        for i in range(self._num_nodes):
            if not visited[i]:
                stack.append(i)
                while stack:
                    node_index = stack.pop()
                    visited[node_index] = True
                    print('index: {}, node: {}'.format(node_index, self._vextexs[node_index].value))
                    edge = self._vextexs[node_index].first
                    while edge:
                        #if self._directed or node_index < edge.vextex: # 无向图只遍历小节点号在前的
                        if self._weighted:
                            print('edge: {} - {}, weight: {}'.format(node_index, edge.vextex, edge.weight))
                        else:
                            print('edge: {} - {}'.format(node_index, edge.vextex))
                        if not visited[edge.vextex]:
                            stack.append(edge.vextex)
                            break
                        edge = edge.next

    def dfs_recursive_print(self):
        visited = [False] * self._num_nodes
        for i in range(self._num_nodes):
            self._dfs_recursive_print_internal(i, visited)

    def _dfs_recursive_print_internal(self, node_index: int, visited: list):
        if visited[node_index]: return
        visited[node_index] = True
        print('index: {}, node: {}'.format(node_index, self._vextexs[node_index].value))
        edge = self._vextexs[node_index].first
        while edge:
            #if self._directed or node_index < edge.vextex: # 无向图只遍历小节点号在前的
            print('edge: {} - {}'.format(node_index, edge.vextex))
            if not visited[edge.vextex]:
                self._dfs_recursive_print_internal(edge.vextex, visited)
                break
            edge = edge.next

    def add_node(self, value):
        self._vextexs.append(VextexNode(value))
        self._num_nodes += 1

    def add_edge(self, vextex_value_start, vextex_value_end, weight=0):
        if self._vextexs[vextex_value_start].first is None:
            self._vextexs[vextex_value_start].first = EdgeNode(vextex=vextex_value_end, weight=weight)
        else:
            edge = self._vextexs[vextex_value_start].first
            while edge.next:
                edge = edge.next
            edge.next = EdgeNode(vextex=vextex_value_end, weight=weight)
        self._num_edges += 1

    def _min_dist(self, dist, visited):
        min = sys.maxsize
        for v in range(self.num_nodes()):
            if not visited[v] and dist[v] < min:
                min = dist[v]
                min_index = v
        return min_index

    def _get_weight(self, u, v):
        edge = self._vextexs[u].first
        while edge:
            if edge.vextex == v and edge.weight > 0:
                return edge.weight
            edge = edge.next
        return -1

    def dijkstra(self, source: int):
        """
        单源最短路径 O(n*n)
        狄克斯特拉算法dijkstra

        G={V,E}
        1. 初始时令 S={V0},T=V-S={其余顶点}，T中顶点对应的距离值
        若存在<V0,Vi>，d(V0,Vi)为<V0,Vi>弧上的权值
        若不存在<V0,Vi>，d(V0,Vi)为∞
        2. 从T中选取一个与S中顶点有关联边且权值最小的顶点W，加入到S中
        3. 对其余T中顶点的距离值进行修改：若加进W作中间顶点，从V0到Vi的距离值缩短，则修改此距离值
        重复上述步骤2、3，直到S中包含所有顶点，即W=Vi为止
        """
        dist = [sys.maxsize] * self.num_nodes()
        dist[source] = 0
        visited = [False] * self.num_nodes()

        for _ in range(self._num_nodes):
            u = self._min_dist(dist, visited)

            visited[u] = True

            for v in range(self._num_nodes):
                w = self._get_weight(u, v)
                if visited[v] == False and w > 0 and dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
        return dist

    def dijkstra_heap(self, source: int) -> list:
        """
        单源最短路径，使用最小堆 O((n+m)log(n))
        """
        q = queue.PriorityQueue(self.num_nodes())
        dist = [sys.maxsize] * self.num_nodes()
        q.put((0, source))
        
        while not q.empty():
            u = q.get()
            if dist[u[1]] < u[0]:
                continue
            dist[u[1]] = u[0]
            u = u[1]

            for v in range(self._num_nodes):
                w = self._get_weight(u, v)
                if w > 0 and dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    q.put((dist[v], v))
        return dist

    def mst_prim(self):
        """
        最小生成树Minimum Spanning Tree
        普里姆算法Prim，使用最小堆 O((n+m)log(n))

        1).输入：一个加权连通图，其中顶点集合为V，边集合为E；
        2).初始化：Vnew = {x}，其中x为集合V中的任一节点（起始点），Enew = {},为空；
        3).重复下列操作，直到Vnew = V：
            a.在集合E中选取权值最小的边<u, v>，其中u为集合Vnew中的元素，而v不在Vnew集合当中，并且v∈V（如果存在有多条满足前述条件即具有相同权值的边，则可任意选取其中之一）；
            b.将v加入集合Vnew中，将<u, v>边加入集合Enew中；
        4).输出：使用集合Vnew和Enew来描述所得到的最小生成树。
        """
        q = queue.PriorityQueue()
        mst = AdjList(directed=self._directed, weighted=self._weighted)
        visited = set()
        v_dict = {} # 原图顶点下标和mst图顶点下标映射

        q.put((0, 0, None)) # weight vextex_index edge

        while not q.empty():
            w, v, e = q.get() # weight vextex edge

            if not e:
                # 将树根加入
                visited.add(0)
                mst.add_node(self._vextexs[0].value)
                v_dict[0] = mst.num_nodes() - 1

            else:
                if e.vextex not in visited:
                    # 将weight最小的边（对侧顶点不在visited中）加入mst
                    visited.add(e.vextex)
                    mst.add_node(self._vextexs[e.vextex].value)
                    v_dict[e.vextex] = mst.num_nodes() - 1
                    mst.add_edge(v_dict[v], v_dict[e.vextex], w)
                    # 新加入的顶点
                    v = e.vextex

            # 将顶点v的所有边的weight和对侧顶点（不在visited中）加入q，
            edge = self._vextexs[v].first
            while edge:
                if edge.vextex not in visited:
                    q.put((edge.weight, v, edge))
                edge = edge.next
        return mst
    
    @staticmethod
    def test_graph_1():
        graph = AdjList(False, False)
        for i in range(7):
            graph.add_node('v{}'.format(i))
        graph.add_edge(0, 1)
        graph.add_edge(0, 2)
        graph.add_edge(0, 3)
        graph.add_edge(1, 4)
        graph.add_edge(5, 1)
        graph.add_edge(4, 2)
        graph.add_edge(5, 3)
        graph.add_edge(4, 6)
        graph.add_edge(5, 6)

        graph.add_edge(1, 0)
        graph.add_edge(2, 0)
        graph.add_edge(3, 0)
        graph.add_edge(4, 1)
        graph.add_edge(1, 5)
        graph.add_edge(2, 4)
        graph.add_edge(3, 5)
        graph.add_edge(6, 4)
        graph.add_edge(6, 5)

        return graph

    @staticmethod
    def test_graph_2():
        graph2 = AdjList(True, False)
        for i in range(8):
            graph2.add_node('v{}'.format(i))
        graph2.add_edge(0, 1)
        graph2.add_edge(0, 5)
        graph2.add_edge(1, 2)
        graph2.add_edge(3, 2)
        graph2.add_edge(2, 4)
        graph2.add_edge(2, 6)
        graph2.add_edge(6, 5)
        graph2.add_edge(5, 8)
        graph2.add_edge(7, 5)
        graph2.add_edge(7, 5)
        return graph2

    @staticmethod
    def test_weighted_net():
        graph = AdjList(False, True)
        for i in range(9):
            graph.add_node('v{}'.format(i))
        graph.add_edge(0, 1, 4)
        graph.add_edge(0, 7, 8)
        graph.add_edge(1, 7, 11)
        graph.add_edge(1, 2, 8)
        graph.add_edge(7, 8, 7)
        graph.add_edge(2, 8, 2)
        graph.add_edge(8, 6, 6)
        graph.add_edge(2, 5, 4)
        graph.add_edge(6, 5, 2)
        graph.add_edge(2, 3, 7)
        graph.add_edge(3, 5, 14)
        graph.add_edge(3, 4, 9)
        graph.add_edge(5, 4, 10)
        graph.add_edge(7, 6, 1)

        graph.add_edge(1, 0, 4)
        graph.add_edge(7, 0, 8)
        graph.add_edge(7, 1, 11)
        graph.add_edge(2, 1, 8)
        graph.add_edge(8, 7, 7)
        graph.add_edge(8, 2, 2)
        graph.add_edge(6, 8, 6)
        graph.add_edge(5, 2, 4)
        graph.add_edge(5, 6, 2)
        graph.add_edge(3, 2, 7)
        graph.add_edge(5, 3, 14)
        graph.add_edge(4, 3, 9)
        graph.add_edge(4, 5, 10)
        graph.add_edge(6, 7, 1)

        return graph

    @staticmethod
    def test_weighted_net_2():
        graph = AdjList(False, True)
        for i in range(6):
            graph.add_node('v{}'.format(i))
        graph.add_edge(0, 1, 1)
        graph.add_edge(0, 2, 12)
        graph.add_edge(1, 3, 3)
        graph.add_edge(1, 2, 9)
        graph.add_edge(3, 2, 4)
        graph.add_edge(3, 4, 13)
        graph.add_edge(2, 4, 5)
        graph.add_edge(4, 5, 4)
        graph.add_edge(3, 5, 15)

        graph.add_edge(1, 0, 1)
        graph.add_edge(2, 0, 12)
        graph.add_edge(3, 1, 3)
        graph.add_edge(2, 1, 9)
        graph.add_edge(2, 3, 4)
        graph.add_edge(4, 3, 13)
        graph.add_edge(4, 2, 5)
        graph.add_edge(5, 4, 4)
        graph.add_edge(5, 3, 15)

        return graph


if __name__ == '__main__':
    """
    graph = AdjList.test_graph_2()
    print('--bfs print--')
    graph.bfs_print()
    print('--dfs print--')
    graph.dfs_print()
    print('--dfs recursive print--')
    graph.dfs_recursive_print()
    """

    graph1 = AdjList.test_weighted_net()
    #print(graph1.dijkstra_heap(0))
    mst = graph1.mst_prim()
    mst.bfs_print()

    