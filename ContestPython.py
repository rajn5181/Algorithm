# import math
# from itertools import combinations
# from collections import defaultdict, Counter, deque
# from math import sqrt, log10, log, floor, factorial, gcd, ceil
# from bisect import bisect_left, bisect_right, insort
# from itertools import permutations, combinations
# import sys
# import io
# import os
# from queue import PriorityQueue, Queue
# input = sys.stdin.readline
# # input=io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
# # sys.setrecursionlimit(10000)
# inf = float('inf')
# mod = 10 ** 9 + 7
#----------------------power formula-----------------------
# def PowerFormula(a, n):
#     if n == 0:
#         return 1

#     val = PowerFormula(a, n // 2)
#     if n % 2 == 0:
#         return val * val
#     else:
#         return val * val * a



# ----------Segment Tree Implementations---------------------------------







#-----------------------Segment Tree End------------------------------------------- 
# Sliding window algorithm


# def Slidingwindow(arr, k):
#     window = sum(arr[:k])
#     max_sum = window
#     n = len(arr)
#     for i in range(n-k):
#         window = window-arr[i]+arr[i+k]
#         max_sum = max(window, max_sum)
#     return max_sum
# # Longest subsequence string


# def lcm(string1, string2, l1, l2):
#     if l1 == 0 or l2 == 0:
#         return 0
#     elif string1[l1-1] == string2[l2-1]:
#         return 1+lcm(string1, string2, l1-1, l2-1)
#     else:
#         return max(lcm(string1, string2, l1-1, l2), lcm(string1, string2, l1, l2-1))
# # Binary search algorithm


# def binary_search(arr, x, low, high):
#     if low <= high:
#         mid = (low+high)//2
#         if arr[mid] == x:
#             return mid
#         elif arr[mid] > x:
#             return binary_search(arr, x, low, mid-1)
#         else:
#             return binary_search(arr, x, mid+1, high)
#     else:
#         return -1

# # All substring from string


# def Allsub_string(srt):
#     res = [srt[x:y] for x, y in combinations(range(len(srt)+1), r=2)]
#     return res

# # Check whether number is prime or not is given list-------------------------------------------


# def is_prime(n):
#     if n < 2:
#         return False
#     i = 2
#     while i * i <= n:
#         if n % i == 0:
#             return False
#         i += 1
#     return True


# # Find Gcd of given number(Greatest common factor)--------------------------


# def Gcd(n1, n2):
#     while n2:
#         n1, n2 = n2, n1 % n2
#     return n1

# # Number of prime number--------------------------------


# def Prime_number(n):  # Sieve algorithm
#     list_numbers = n*[True]
#     list_numbers[0] = list_numbers[1] = False
#     square_root = int(math.sqrt(n))
#     for p in range(square_root):
#         if list_numbers[p] == True:
#             for i in range(p*p, n, p):
#                 list_numbers[i] = False
#     for p in range(len(list_numbers)):
#         if list_numbers[p] == True:
#             print(p, end=" ")
# # Prime factor of Number-----------------------------------


# def primeFactors(n):
#     while n % 2 == 0:
#         print(2, end=" ")
#         n = n / 2
#     for i in range(3, int(math.sqrt(n))+1, 2):
#         while n % i == 0:
#             print(i, end=" ")
#             n = n / i
#     if n > 2:
#         print(int(n), end=" ")

# find all factors of number -------------------------------
# def find_factors(n):
#     factors = []
#     i = 1
#     while i * i <= n:
#         if n % i == 0:
#             factors.append(i)
#             if i != n // i:
#                 factors.append(n // i)
#         i += 1
#     return factors
# Solve rajn5181-----------------------------------------------------------
for _ in range(int(input())):
    n = int(input())
    p = []
    np = []
    for i in range(1, n + 1):
        if is_prime(i):
            p.append(i)
        else:
            np.append(i)
    p = p[::-1]
    np = np[::-1]
    p.extend(np)
    print(*p)
