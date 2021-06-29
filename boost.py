answer = dict()
result = []

def sol(result):
    for i in range(len(result)):
        result[i] = str(result[i]).replace("'","")
    print(result)

def solution(param0):
    fName, extend = param0.split(".")
    if extend[-1]==']':
        extend = extend[:-1]
    fName = fName[0]+"."+extend[:-1]

    if fName in answer.keys():
        answer[fName] += 1
    else:
        answer[fName] = 1
    if int(answer[fName])>=2:
        result.append('"'+fName+'"')
        result.append(answer[fName])
    

def findFile(f):
    drctry = f.split("/")
    finalFile = drctry[-1]
    solution(finalFile)

files = input().split(",")
for i in range(len(files)):
    findFile(files[i])
sol(result)
#["/a/a_v2.x", "/b/a.x", "/c/t.z"]
