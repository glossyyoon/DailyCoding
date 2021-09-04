a = int(input())
t = int(input())
bun = int(input())
people = [i for i in range(a)]
p = 0
n = 2  # 횟수
count = 1


def solution(p):
    initP = p
    n = 2  # 횟수
    count = 1
    print(people[p % a])
    for j in range(10000):
        if count == t:
            return people[p % a]
        p += 2
        count += 1
        # print(people[p % a])
        if count == t:
            return people[p % a]
        p += 1
        if initP == 0:
            for i in range(n):
                p += 1
                count += 1
                print(people[p % a])
                if count == t:
                    return people[p % a]
            p = p + n
            p += 1
            count += 1
            print(people[p % a])
        elif initP == 1:
            p = p + n
            for i in range(n):
                p += 1
                count += 1
                print(people[p % a])
                if count == t:
                    return people[p % a]
            p += 1
            count += 1
            if count == t:
                return people[p % a]

        n += 1


if bun == 0:
    print(solution(0))
elif bun == 1:
    print(solution(1))
