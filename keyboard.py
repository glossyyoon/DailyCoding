keyboard = [["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"],
            ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
            ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
            ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "?"]]
positions = []
result = ""


def output(keyboard):
    s = list(input())
    for a in s:
        save(a, positions)
    temp = [0, -1]
    print(find(positions, temp, ""))


def find(positions, temp, result):
    temp[1] += 1
    for position in positions:

        while position[0] != temp[0] or position[1] != temp[1]:
            print("temp=", temp, "position=", position)
            if temp[0] > position[0]:
                result += "^"
                temp[0] -= 1
                continue
            if temp[0] < position[0]:
                result += "_"
                temp[0] += 1
                continue
            if temp[1] < position[1]:
                result += ">"
                temp[1] += 1
                continue
            if temp[1] > position[1]:
                result += "<"
                temp[1] -= 1
                continue
        if temp[0] == position[0] and temp[1] == position[1]:
            result += "@"
    return result


def save(a, positions):
    for i in range(4):
        for j in range(10):
            if a == keyboard[i][j]:
                positions.append([i, j])


output(keyboard)
print(result)