class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        l = 0
        countS1, countS2 = {}, {}
        for i in range(len(s1)):
            countS1[s1[i]] = countS1.get(s1[i], 0) + 1
        
        for r in range(len(s2)):
            countS2[s2[r]] = countS2.get(s2[r], 0) + 1
            if r - l + 1 > len(s1):
                countS2[s2[l]] -= 1
                if countS2[s2[l]] == 0:
                    del countS2[s2[l]]
                l += 1
            if r - l + 1 == len(s1):
                if countS1 == countS2:
                    return True
        return False            


