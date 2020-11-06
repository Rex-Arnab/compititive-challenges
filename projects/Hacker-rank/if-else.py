
#! Task
# Given an integer, n, perform the following conditional actions:

#* If n is odd, print Weird
#* If n is even and in the inclusive range of  to , print Not Weird
#* If n is even and in the inclusive range of  to , print Weird
#* If n is even and greater than , print Not Weird
#! Input Format
# A single line containing a positive integer, .

# !Constraints
#? 1 <= n <= 100

# Output Format

# Print Weird if the number is weird. Otherwise, print Not Weird.
n = int(input().strip())
print("Not Weird") if n%2==0 else print("Weird")