a = [10, 23, 53, 2, 9]
#제일 작은 값 찾기
#제일 큰 값 찾기
#합계 구하기
small = a[0]
large = a[0]
hap = 0
for i in a:
    if small > i:
        small = i
    if large < i:
        large = i
    hap += i
print("small=", small)
print("large=", large)
print("hap=", hap)

# small = min(a)
# large = max(a)
# hap = sum(a)

# print("small=", small)
# print("large=", large)
# print("hap=", hap)