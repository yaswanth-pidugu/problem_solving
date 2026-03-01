class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        r = len(s) - 1
        while r >= 0:
            if s[r] in ('a', 'e', 'i', 'o', 'u'):
                r-=1
            else:
                break
        return s[:r+1]