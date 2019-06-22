import sys
import fractions
stdin = sys.stdin

def li(): return map(int, stdin.readline().split())
A, B, C, D = tuple(li())
def helper(A, B, C):
    return (B) // C - (A-1) // C
num1 = helper(A, B, C)
num2 = helper(A, B, D)
num3 = helper(A, B, C * D // fractions.gcd(C, D))
delta = num1 + num2 - num3
print(B - A + 1 - delta)
