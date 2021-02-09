import collections
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
anagram = collections.defaultdict(list)
for word in strs:
    anagram[''.join(sorted(word))].append(word)
print(anagram.values())