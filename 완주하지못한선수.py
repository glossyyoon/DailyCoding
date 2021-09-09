import collections
def solution(participant, completion):
    i = 0
    while len(completion)>0:
        if participant[i] in completion:
            participant.pop(i)
            completion.pop(completion.index(participant[i]))
        i += 1
        print(participant)
    return participant
print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))