#!/usr/bin/env python
# coding=utf-8
'''
Author: uniooo
Date: 2021-05-18 11:11:31
LastEditors: uniooo
LastEditTime: 2021-06-02 12:03:06
FilePath: /graph_tools/check_edge_consecutive.py
Description: check if the graph data is id-consecutive.
    1. read graph and compute the number of vertices, edges. compare 
    it with the claimed numbers in the graph file.
    2. check the vertices' ids. if not consecutive, remap the ids to
    new ids. output the graph with new ids and the mapping relation.
'''
import sys  

class GraphChecker:
    def __init__(self):
        self.adj = {}
        self.vtex_set = set()
        self.n_claim = 0
        self.m_claim = 0
        self.file_name = None

    def add_edge(self, a, b):
        if a > b:
            a, b = b, a
        if a in self.adj:
            self.adj[a].add(b)
        else:
            self.adj[a] = set([b])
        self.add_vertex(a)
        self.add_vertex(b)
        
    def add_vertex(self, a):
        self.vtex_set.add(a)

    def read_graph(self, fin_name):
        self.file_name = fin_name
        with open(fin_name, "r") as fin:
            self.n_claim, self.m_claim = map(int, next(fin).strip().split())
            m_direct_count = 0
            for line in fin:
                a, b = map(int, line.strip().split()[:2])   # only take the first two cols as (u,v)
                self.add_edge(a, b)
                m_direct_count += 1
            if m_direct_count != self.m_claim:
                print("m_direct_count = %d, m_claim = %d" % (m_direct_count, self.m_claim))
    
    def check_vertex(self):
        n_count = len(self.vtex_set)
        if n_count != self.n_claim:
            print("n_count = %d, m_claim = %d" % (n_count, self.m_claim))
        
        if min(self.vtex_set) != 1:
            print("vertex id does not start with 1")
            return False

        if n_count != max(self.vtex_set):
            print("vertex id is not consecutive")
            return False
        
    def remapping_graph(self):
        n_count = len(self.vtex_set)
        vtex_list = sorted(list(self.vtex_set))  # new_id -1 --> old_id
        old_id2new_id = [0] * (max(self.vtex_set) + 1)
        cnt = 0
        for vid in vtex_list:
            cnt += 1
            old_id2new_id[vid] = cnt
        
        edge_list = []
        for vid in self.adj:
            for uid in self.adj[vid]:
                edge_list.append((old_id2new_id[vid], old_id2new_id[uid]))

        edge_list = sorted(edge_list)
        # print(len(edge_list))
        with open(self.file_name+".new", "w") as fout:
            fout.write(str(n_count) + " " + str(len(edge_list)) + "\n")
            for a, b in edge_list:
                fout.write(str(a) + " " + str(b) + "\n")

        print("New graph file is written to disk as " + self.file_name + ".new\n")

        #     for vid in self.adj:
        #         for uid in self.adj[vid]:
        #             fout.write(str(old_id2new_id[vid]) + " " + str(old_id2new_id[uid]) + "\n")
            
def main():
    if len(sys.argv) != 2:
        print("./check_edge_consecutive.py fin_name\n")
        exit(0)

    fin_name =  sys.argv[1]
    ck = GraphChecker()
    ck.read_graph(fin_name)
    if not ck.check_vertex(): 
        ck.remapping_graph()

if __name__ == "__main__":
    main()