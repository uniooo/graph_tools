#!/usr/bin/env python
# coding=utf-8
'''
Author: uniooo
Date: 2021-05-19 14:48:19
LastEditors: uniooo
LastEditTime: 2021-06-01 15:55:24
FilePath: /graph_tools/count_ccs.py
Description: 
'''

import sys
sys.setrecursionlimit(5000)

class CC_Counter:
    def __init__(self, _n) -> None:
        self.n = _n
        self.pa = [-1] * (self.n+1)

    def find_pa(self, node):
        if self.pa[node] == -1:
            return node
        else:
            self.pa[node] = self.find_pa(self.pa[node])
            return self.pa[node]

    def union_node(self, u, v):
        u = self.find_pa(u)
        v = self.find_pa(v)
        if (u != v):
            self.pa[v] = u

    def count_cc(self, edges):
        for u, v in edges:
            self.union_node(u,v)
            
        cnt = 0
        for i in range(self.n):
            if self.pa[i] == -1:
                cnt += 1
        return cnt-1 # node id starts from 1, hence 0 is always -1.

def count_ccs(graph_file):
    with open(graph_file, "r") as fin:
        n, m = map(int, next(fin).strip().split())
        cc_counter = CC_Counter(n)
        
        read_edges = lambda fin:(map(int, line.strip().split()) for line in fin)
        edges = read_edges(fin)
        return cc_counter.count_cc(edges)
        
if __name__ == "__main__":
    graph_file = sys.argv[1]
    num_of_ccs = count_ccs(graph_file)
    print(num_of_ccs)

