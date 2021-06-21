a = int(input())
# for i in range(1, a + 1):
#     if i % 3 == 0:
#         print("x", end=" ")
#     else:
#         print(i, end=" ")
count = 1
while count != a + 1:
    if count % 3 == 0:
        print("x", end=" ")
    else:
        print(count, end=" ")
    count += 1
