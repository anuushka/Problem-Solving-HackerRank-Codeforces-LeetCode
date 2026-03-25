'''
Task

Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.

Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.

Input Format
Read year, the year to test.
1990

Constraints
1900 <= year <= 10^5

Output Format
The function must return a Boolean value (True/False). 
Output is handled by the provided code stub.
False
'''

def is_leap(year):
    leap = False
    check = lambda x: (x % 4 == 0 and x % 100 != 0) or ( x % 400 == 0)
    leap = check(year)
    return leap

year = int(input())
print(is_leap(year))
