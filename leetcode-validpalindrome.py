class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for character in s:
            if character.isalnum(): #isalnum(): 영문자, 숫자를 판별하는 함수
                strs.append(character.lower())
        while len(strs)>1:
            if strs.pop(0) != strs.pop():
                return False
        return True