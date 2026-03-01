class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        r = len(s)-1
        while r >=0 and s[r] in "aeiou":
            r-=1
        return s[:r+1]