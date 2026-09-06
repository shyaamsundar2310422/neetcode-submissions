class Solution:
    def isValid(self, s: str) -> bool:
        n=len(s)
        stack=[]
        for i in range(n):
            if s[i] in "({[":
                stack.append(s[i])
            else:
                if not stack:
                    return False
            
                top=stack[-1]
                if s[i]=="]" and top =="[":
                    stack.pop()
                elif s[i]==")" and top=="(":
                    stack.pop()
                elif s[i]=="}" and top=="{":
                    stack.pop()
                else:
                    return False
        return not stack

