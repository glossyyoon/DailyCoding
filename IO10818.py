num1 = int(input())
num_list = list(map(int, input().split(" ")))
print('{} {}'.format(min(num_list), max(num_list)))