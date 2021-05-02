def isPrime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


m = int(input())
n = list(map(int, input().split()))
ans = 0
for i in n:
    if isPrime(i):
        ans += 1
print(ans)