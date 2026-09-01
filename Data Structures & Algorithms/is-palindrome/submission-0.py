class Solution:
    def isPalindrome(self, s: str) -> bool:
        t=[]
        for i in s:
            if i.isalnum():
                t.append(i.lower())
        return t==t[::-1]
        