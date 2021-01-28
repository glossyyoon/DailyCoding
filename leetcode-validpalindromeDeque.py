class Solution:
    def isPalindrome(self, s:str)-> bool:
        strs: Deque = collections.deque()
            
        for character in s:
            if character.isalnum():
                strs.append(character.lower())
                
        while len(strs)>1:
            if strs.pop()!= strs.popleft():
                return False
        return True