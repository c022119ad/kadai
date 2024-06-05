from collections import deque
from dataclasses import dataclass, field
import sys
import heapq


@dataclass
class Node:
    id_: int
    name: str = field(default="hoge")
    coord: tuple = field(default_factory=tuple,repr=False)

    
    adj_nodes: list = field(default_factory=list, repr=False)
    dist: float = field(default=-1)
    
    parent:list = field(default=None,repr=False)


class Graph:
    def __init__(self, node_file_path, edge_file_path):
        self.nodes: list[Node] = __class__.read_graph(node_file_path, edge_file_path)

    @staticmethod
    def read_graph(node_file_path, edge_file_path):
        nodes = list()
        with open(node_file_path, "r", encoding="utf-8") as rfo:
            for i, row in enumerate(rfo):
                col = row.rstrip().split("\t")
                name = col[1]
                lat, lng = col[3].split(",")
                nodes.append(Node(i, name, (float(lat), float(lng))))
        with open(edge_file_path, "r") as rfo:
            num_of_nodes, num_of_edges = rfo.readline().rstrip().split()
            if int(num_of_nodes) != len(nodes):
                raise Exception("ノード数不一致", num_of_nodes, len(nodes))
            for row in rfo:
                from_, to_ = row.rstrip().split()
                nodes[int(from_)-1].adj_nodes.append(int(to_)-1)
        return nodes

    @staticmethod
    def calc_distance(node1: Node, node2: Node) -> float:
        coord1 = node1.coord
        coord2 = node2.coord
        return ((coord1[0]-coord2[0])**2 + (coord1[1]-coord2[1])**2)**0.5
    
    def dijkstra(self,start_id):
        que = []
        start:Node =self.nodes[start_id]
        start.dist = 0
        heapq.heappush(que,(start.dist,start))
        while True:
            if len(que)==0:
                break
            current = heapq.heappop(que)
            node = current.adj_nodes
            nodedist = current.dist + Graph.calc_distance(current,node)
            if node.dist == None:
                node.dist = nodedist
                heapq.heappush(que,(node.dist,node))
                node.parent = current
            elif node.dist != None and node.dist > nodedist:
                node.dist = nodedist
                node.parent = current
    
    def shortest_path(self,start_id,goal_id):
        Graph.dijkstra(self,start_id)
        stls = Stack()
        nowid = goal_id
        #stls.push(self.nodes[goal_id])
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
    
    #print(sys.argv[1],sys.argv[2])
    #graph = Graph(sys.argv[1], sys.argv[2])  # data/station_nodes.txt, data/station_edges.txt
    #start_id = int(sys.argv[3])-1  # 1265（八王子駅）から
    #goal_id = int(sys.argv[4])-1  # 4894（湘南台駅）／6527（つくば駅）までの経路
    graph = Graph("data/station_nodes.txt", "data/station_edges.txt")  # data/station_nodes.txt, data/station_edges.txt
    start_id = int(1265)-1  # 1265（八王子駅）から
    goal_id = int(4894)-1  # 4894（湘南台駅）／6527（つくば駅）までの経路
    graph.shortest_path(start_id, goal_id)
