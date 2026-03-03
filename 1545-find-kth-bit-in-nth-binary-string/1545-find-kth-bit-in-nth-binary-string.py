class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return "0"
        mid = 1 << (n - 1)
        if mid == k:
            return "1"
        if mid > k:
            return self.findKthBit(n - 1, k)
        mirror = (1 << n) - k
        bits = self.findKthBit(n - 1, mirror)
        return "1" if bits == "0" else "0"