'''
Input:
The first line of input contains the original string. The next line contains the substring.

Output: 
Output the integer number indicating the total number of occurrences of the substring in the original string.

Example: 
ABCDCDC
CDC

Output
2

This algorithm is Naive method.
'''

def count_substring(string, sub_string):
    pattern = []
    count = 0
    N = len(string)
    M = len(sub_string)
    for i in range(N - M + 1):
        for j in range(M):
            if (string[i+j] != sub_string[j]):
                break
        else:
            pattern.append(i+1)
    count = len(pattern)
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
