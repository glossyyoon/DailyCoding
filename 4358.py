import sys

trees = {}
n = 0
while True:
    s = sys.stdin.readline().rstrip()
    if s == "":
        break
    else:
        if s in trees:
            trees[s] += 1
        else:
            trees[s] = 1
        n += 1
l = list(trees.keys())
l.sort()
for tree in l:
    print(tree, "%.4f" % (trees[tree] / n * 100))
