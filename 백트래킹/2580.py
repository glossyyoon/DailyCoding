import sys

sdoku = [list(map(int, sys.stdin.readline().rstrip().split())) for i in range(9)]
def backtrack(start, comb):
    if comb==0:
        return
    for i in range(start, 10):
        comb.append(i)
        backtrack(i+1, comb)
        comb.pop()
    
