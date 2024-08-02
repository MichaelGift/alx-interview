#!/usr/bin/python3
"""The N queens puzzle is the challenge of placing N non-attacking queens on an
N×N chessboard. Write a program that solves the N queens problem. The program
should take N as a command-line argument and print the solution to the problem.
"""
import sys


if len(sys.argv) > 2 or len(sys.argv) < 2:
    print("Usage: nqueens N")
    exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)

n = int(sys.argv[1])


def findPositions(n, i=0, a=[], b=[], c=[]):
    """ find positions """
    if i < n:
        for j in range(n):
            if j not in a and i + j not in b and i - j not in c:
                yield from findPositions(n, i + 1, a + [j], b + [i + j], c + [i - j])
    else:
        yield a


def solveNQueens(n):
    """ solve n queens """
    k = []
    i = 0
    for solution in findPositions(n, 0):
        for s in solution:
            k.append([i, s])
            i += 1
        print(k)
        k = []
        i = 0


solveNQueens(n)
