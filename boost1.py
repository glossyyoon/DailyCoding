def solution(param0):
    answer = []
    for param in param0:
        name, h = param.split('.')
        name = name.split('/')[-1]
        name = name.split('_')[0]
        file = name + '.' + h
        print(file)
    return answer
solution(["/a/a_v2.x", "/b/a.x", "/c/t.z"])