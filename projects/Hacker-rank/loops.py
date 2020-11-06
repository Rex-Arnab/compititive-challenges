
#! Task
#* The provided code stub reads and integer, n, from STDIN. For all non-negative integers , i < n, print i^2.

#* Example
#* n = 3
#? Output:
#? 0
#? 1
#? 4

#!Constraints
#! 1 <= n <= 20

if __name__ == '__main__':
    n = int(input())
    if (1 <= n and n <= 20):
        for i in range(n):
            print(i**2)