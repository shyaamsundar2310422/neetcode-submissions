from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        s1_count = Counter(s1)
        window_count = {}
        k = len(s1)

        for i in range(k):
            ch=s2[i]
            window_count[ch]=window_count.get(ch,0) + 1
        
        if s1_count==window_count:
            return True

        
        for right in range(k,len(s2)):
            outgoing=s2[right-k]
            window_count[outgoing]-=1

            if window_count[outgoing]==0:
                del window_count[outgoing]

            incoming=s2[right]
            window_count[incoming]=window_count.get(incoming,0)+1
            
            if s1_count==window_count:
                return True

        return False



        
