#!/usr/bin/env python
# coding=utf-8
'''
@Author: uniooo
@Date: 2020-05-10 15:03:27
@LastEditors: uniooo
@LastEditTime: 2020-05-10 16:00:08
@Description: to check that no single direct edge in the edge data.
'''

import sys
import re

def check_edges_one2many(finedges_):
    '''
    @description: check the one2many style graph edges. The nodes start
                from 0, and are continuously marked with numbers. Each line is the 
                neighbor node ids of corresponding node. Line number equals to the 
                node id + 1.
    @param {finedges_} 
    @return: None.
    '''
    with open(finedges_, "r") as finedges:
        i = 0
        edge_set = set()
        for line in finedges:
            items = map(lambda x: int(x.strip()), line.split())
            for item in items:
                #TODO add repeat check
                edge_set.add((i, item))
            i += 1

        flag = True
        for (a,b) in edge_set:
            if (b,a) not in edge_set:
                print("Wrong data set: %s %s" % (a, b))
                flag = False
        if flag:
            print("Done without mistake!")

def check_edges_one2one(finedges_):
    '''
    @description: check the one2one style graph edges. Each line is an edge.
    @param {type} 
    @return: 
    '''
    # TODO
    with open(finedges_, "r") as finedges:
        edge_set = set()
        for line in finedges:
            a, b = map(lambda x: int(x.strip()), re.split(r'\s*[,\s]\s*', line.strip())) #using re.split to enable both space and comma
            # TODO add repeat check
            edge_set.add((a,b))
            
        flag = True
        for (a,b) in edge_set:
            if (b,a) not in edge_set:
                print("Wrong data set: %s %s" % (a,b))
                flag = False
        if flag:
            print("Done without mistake!")
            
def main(finedges_, file_type):
    if file_type == 0:
        check_edges_one2many(finedges_)
    else:
        check_edges_one2one(finedges_)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        finedges_ = sys.argv[1]
        main(finedges_, 0)
    elif len(sys.argv) == 3:
        finedges_ = sys.argv[1]
        file_type = int(sys.argv[2])
        main(finedges_, file_type)
    else:        
        print("input:  checker filename filetype\n\tfiletype:0: one2many (default)\n\t\t 1: one2one\n")
