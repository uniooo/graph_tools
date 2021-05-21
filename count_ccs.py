#!/usr/bin/env python
# coding=utf-8
'''
Author: uniooo
Date: 2021-05-19 14:48:19
LastEditors: uniooo
LastEditTime: 2021-05-21 11:56:39
FilePath: /graph_tools/count_ccs.py
Description: 
'''

import sys
sys.setrecursionlimit(5000)

def find_pa(node):
   if pa[node] == -1:
       return node
   else:
       pa[node] = find_pa(pa[node])
       return pa[node]

def union_node(u, v):
    u = find_pa(u)
    v = find_pa(v)
    if (u != v):
        pa[v] = u
    
graph_file = sys.argv[1]
with open(graph_file, "r") as fin:
    n, m = map(int, next(fin).strip().split())
    
    pa = [-1] * (n+1)
    
    for line in fin:
        u, v = map(int, line.strip().split())
        union_node(u,v)
    
    cnt = 0
    for i in range(len(pa)):
        if pa[i] == -1:
            cnt += 1
    print(cnt-1)
    
    

