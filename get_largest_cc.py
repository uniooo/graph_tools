#!/usr/bin/env python
# coding=utf-8
'''
Author: uniooo
Date: 2021-06-01 11:28:56
LastEditors: uniooo
LastEditTime: 2021-06-03 10:15:06
FilePath: /graph_tools/get_largest_cc.py
Description: 
'''

import sys
from count_ccs import get_ccs
from collections import Counter

from check_edge_consecutive import GraphChecker

def get_largest_cc(filename):
    cnt, n, cc_id = get_ccs(filename)
    if cnt == 1:
        print("Only 1 connected components\n")
        return
    result = Counter(cc_id[1:])
    largest_id = max(result, key=result.get)
    included_vertex = set()
    included_vertex.add(largest_id)
    for i in range(1,n+1):
        if cc_id[i] == largest_id:
            included_vertex.add(i)
    
    ck = GraphChecker()
    with open(filename, "r") as fin:
        read_edges = lambda fin: (map(int, line.strip().split()) for line in fin)
        edge_list = read_edges(fin)
        included_edge_list = [(u,v) for u,v in edge_list if (u in included_vertex and v in included_vertex)]
        ck.set_graph_by_edges(included_edge_list)
        edge_list = ck.remapping_graph()
        with open(filename+".largestCC", "w") as fout:
            fout.write(str(len(included_vertex)) + " " + str(len(edge_list)) + "\n")
            for a, b in edge_list:
                fout.write(str(a) + " " + str(b) + "\n")

        print("New graph file with largest CC is written to disk as " + filename + ".largestCC\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("./" + sys.argv[0] + " graph_file\n")
        exit(0)
    
    get_largest_cc(sys.argv[1])