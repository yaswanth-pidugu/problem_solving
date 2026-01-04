class Solution:
    def largestEven(self, s: str) -> str:
        if len(s) == 1:
            if s == "2":return s
            else: return ""
        for i in range(len(s)-1,-1,-1):
            if s[i] == "2":
                return s[:i+1]
        return ""