import sys

if len(sys.argv) != 2:
    print("./count_unique graphname") 
graphname = sys.argv[1]
with open(graphname, "r") as fin:
    m = next(fin)
    mm = []
    for line in fin:
        a, b = map(int, line.strip().split())
        mm.append(a)
        mm.append(b)
    mset = set(mm)
    print(len(mset))
