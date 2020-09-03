import sys
sys.stdin = open("input.txt", 'r')
s = input()
k = input()
print(int(k in s))