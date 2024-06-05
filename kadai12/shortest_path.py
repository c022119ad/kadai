from collections import deque
from dataclasses import dataclass, field
import sys


@dataclass
class Node:
    id_: int
    name: str = field(default="hoge")
    adj_nodes: list = field(default_factory=list, repr=False)
    dist: int = field(default=-1)
    parent:list =field(default=None,repr=0)


class Graph:
    def __init__(self, node_file_path, edge_file_path):
        self.nodes: list[Node] = __class__.read_graph(node_file_path, edge_file_path)

    @staticmethod
    def read_graph(node_file_path, edge_file_path):
        nodes = list()
        with open(node_file_path, "r", encoding="utf-8") as rfo:
            for i, row in enumerate(rfo):
                name = row.rstrip().split("\t")[1]
                nodes.append(Node(i, name))
        with open(edge_file_path, "r") as rfo:
            num_of_nodes, num_of_edges = rfo.readline().rstrip().split()
            if int(num_of_nodes) != len(nodes):
                raise Exception("ノード数不一致", num_of_nodes, len(nodes))
            for row in rfo:
                from_, to_ = row.rstrip().split()
                nodes[int(from_)-1].adj_nodes.append(int(to_)-1)
        return nodes

    def bfs(self, start_id,goal_id):
        start: Node = self.nodes[start_id]
        start.dist = 0
        que = deque()
        que.append(start)
        while True:
            try:
                current = que.popleft()
            except:
                break
            for node_id in current.adj_nodes:
                node = self.nodes[node_id]
                if node.dist != -1:
                    continue
                node.dist = current.dist+1
                que.append(node)
                node.parent=current
            if node.id_ == goal_id:
                break

    def shortest_path(self,start_id,goal_id):
        Graph.bfs(self,start_id,goal_id)
        stls = Stack()
        nowid = goal_id
        stls.push(self.nodes[goal_id])
        while nowid != start_id: 
            nownode = self.nodes[nowid]
            nowmon = nownode.parent
            stls.push(nowmon)
            nowid = nowmon.id_
        while len(stls) !=0:
            print(stls.pop())
            
            
class Stack(list):
    def push(self,valu):
        self.append(valu)
            
if __name__ == "__main__":
    graph = Graph(sys.argv[1], sys.argv[2])  # data/station_nodes.txt, data/station_edges.txt
    start_id = int(sys.argv[3])-1  # 1265（八王子駅）から
    goal_id = int(sys.argv[4])-1  # 4894（湘南台駅）／6527（つくば駅）までの経路
    graph.shortest_path(start_id, goal_id)
