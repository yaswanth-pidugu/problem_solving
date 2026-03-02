from typing import List

class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)

        size = 1
        while size < n:
            size <<= 1

        maxT = [-1] * (size * 2)
        sumT = [0] * (size * 2)

        # compute trailing zeros
        for i in range(n):
            trail = 0
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 0:
                    trail += 1
                else:
                    break
            maxT[size + i] = trail
            sumT[size + i] = 1

        # build segment tree
        for i in range(size - 1, 0, -1):
            maxT[i] = max(maxT[i * 2], maxT[i * 2 + 1])
            sumT[i] = sumT[i * 2] + sumT[i * 2 + 1]

        swaps = 0

        for i in range(n):
            req = n - 1 - i

            if maxT[1] < req:
                return -1

            idx = 1

            # find first valid row
            while idx < size:
                if maxT[idx * 2] >= req:
                    idx = idx * 2
                else:
                    swaps += sumT[idx * 2]
                    idx = idx * 2 + 1

            # remove the row
            maxT[idx] = -1
            sumT[idx] = 0

            # update ancestors
            idx //= 2
            while idx:
                maxT[idx] = max(maxT[idx * 2], maxT[idx * 2 + 1])
                sumT[idx] = sumT[idx * 2] + sumT[idx * 2 + 1]
                idx //= 2

        return swaps