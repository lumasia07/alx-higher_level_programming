#!/usr/bin/python3
"""Module to print N queens"""
import sys


class Solver:
    """Defines a class to solver"""
    def __init__(self, n):
        """Inits a function to class Solver"""
        self.n = n
        self.brd = [-1] * n

    def safe_zone(self, i, j):
        """Check if there is a queen in same column"""
        for _ in range(i):
            if self.brd[_] == j or \
                    self.brd[_] - _ == j - i or \
                    self.brd[_] + _ == j + i:
                        return False
        return True

    def solve_queens(self, i):
        """Solve for queens"""
        if i == self.n:
            self.print_sol()
            return

        for j in range(self.n):
            if self.safe_zone(i, j):
                self.brd[i] = j
                self.solve_queens(i + 1)

    def print_sol(self):
        """Prints solution"""
        sol = []
        for i in range(self.n):
            l = ['Q' if _ == self.brd[i] else '.' for _ in range(self.n)]
            sol.append(''.join(l))
        print('\n'.join(sol))
        print()

    @staticmethod
    def nqueens(n):
        if not isinstance(n, int):
            print("N must be a number")
            sys.exit(1)

        if n < 4:
            print("N must be at least 4")
            sys.exit(1)

        s = Solver(n)
        s.solve_queens(0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        Solver.nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
