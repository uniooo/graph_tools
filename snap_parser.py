#!/usr/bin/env python
# coding=utf-8
'''
Author: uniooo
Date: 2022-02-27 19:03:03
LastEditors: uniooo
LastEditTime: 2022-02-28 20:00:37
FilePath: /graph_tools/snap_parser.py
Description: to convert the graph file from SNAP to a general graph file
'''

import sys

class SNAP_Graph:
    def __init__(self) -> None:
        self.adj = {}
        self.vtx_set = set()
        self.fin_name = None
        self.claim_n = 0
        self.claim_m = 0
        self.real_n = 0
        self.real_m = 0

    def add_edge(self, a, b, w = 1): # default weight = 1
        if a > b:
            a, b = b, a
        if a in self.adj:
            if b in self.adj[a]:
                if self.adj[a][b] > w:  # choose the smallest weight
                    self.adj[a][b] = w
            else:
                self.adj[a][b] = w
        else:
            self.adj[a] = {b: w}
        self.add_vtx(a)
        self.add_vtx(b)

    def add_vtx(self, vtx):
        self.vtx_set.add(vtx)
        
    def read_weighted_graph(self, fin_name):
        self.fin_name = fin_name
        with open(fin_name, "r") as fin:
            for line in fin:
                if line.startswith("a"):
                    a, b, w = map(int, line.strip().split()[1:4])
                    self.add_edge(a, b, w)
                elif line.startswith("c"):
                    continue
                elif line.startswith("p"):
                    self.claim_n, self.claim_m = map(int, line.strip().split()[2:4])

    def read_graph(self, fin_name):
        self.fin_name = fin_name
        with open(fin_name, "r") as fin:
            for line in fin:
                if line.startswith("#"):
                    if line.startswith("# Nodes:"):
                        line = line.strip().split()
                        self.claim_n, self.claim_m = int(line[2]), int (line[4])
                else:                    
                    a, b = map(int, line.strip().split())
                    self.add_edge(a, b)
                    
    def remapping_graph(self):
        vtex_list = sorted(list(self.vtx_set))  # new_id -1 --> old_id
        old_id2new_id = [0] * (max(self.vtx_set) + 1)
        cnt = 0
        for vid in vtex_list:
            cnt += 1
            old_id2new_id[vid] = cnt
        
        edge_list = []
        for vid in self.adj:
            for uid in self.adj[vid]:
                edge_list.append((old_id2new_id[vid], old_id2new_id[uid], self.adj[vid][uid]))

        edge_list = sorted(edge_list)
        return edge_list

    def check_graph(self):
        self.real_n = len(self.vtx_set)
        self.edge_list = self.remapping_graph()
        self.real_m = len(self.edge_list)
        print("Claim_n: %d, Claim_m: %d" % (self.claim_n, self.claim_m))
        print("Real_n: %d, Real_m: %d" % (self.real_n, self.real_m))

    def print_edge_list(self):
        with open(self.fin_name+".new", "w") as fout:
            fout.write(str(self.real_n) + " " + str(self.real_m) + "\n")
            for a, b, w in self.edge_list:
                fout.write(str(a) + " " + str(b) + " " + str(w) + "\n")

        print("New graph file is written to disk as " + self.fin_name + ".new\n")        


# def read_snap(graphfile):
#     with open(graphfile, "r") as fin:
#         edge_set = set()
#         for line in fin:
#             if line.startswith("#") or line.startswith("==>"):
#                 continue

#             a, b = list(map(int, line.strip().split()))
#             a, b = (a, b) if a < b else (b, a)
#             edge_set.add((a,b))

#         return edge_set
    


def main():
    # graphfile = "test.txt"
    graphfile = sys.argv[1]
    g = SNAP_Graph()
    g.read_graph(graphfile)
    g.check_graph()
    g.print_edge_list()
    
if __name__ == "__main__":
    main()
