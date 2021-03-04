def main():
    whole, eat, loc = map(int, input().split())
    forStart = list(map(int, input().split()))

    for i in range(len(forStart)):
        forStart[i] = abs(forStart[i] - loc)
    startLoc = min(forStart)
    start = forStart.index(startLoc)

    for i in range(len(forStart)):
        if i != start:
            forStart[i] -= 1
    forStart.sort()
    result = 0
    for i in range(eat):
        result += forStart[i]
    print(result)


if __name__ == "__main__":
    main()