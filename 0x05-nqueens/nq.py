#!/usr/bin/env python3
from typing import List
import sys

class Solution:
    def solveNQueen(self, n: int) -> List[List[List[int]]]:
        def check_input():
            if len(sys.argv) != 2:
                print("Usage: nqueens N")
                sys.exit(1)
            try:
                n = int(sys.argv[1])
            except ValueError:
                print("N must be a number")
                sys.exit(1)
            if n < 4:
                print("N must be at least 4")
                sys.exit(1)
            return n

        n = check_input()

        col = set()
        posDiag = set()  # (r + c)
        negDiag = set()  # (r - c)

        res = []

        def backtrack(r, current_solution):
            if r == n:
                res.append(current_solution[:])
                return

            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                current_solution.append([r, c])

                backtrack(r + 1, current_solution)

                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                current_solution.pop()

        backtrack(0, [])
        return res

if __name__ == "__main__":
    sol = Solution()
    res = sol.solveNQueen(sys.argv[1])

    for solution in res:
        print(solution)
