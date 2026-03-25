''' 
Example
n = 5
Print the string: 12345
'''

if __name__ == '__main__':
    n = int(input())
    print("".join(map(str, range(1, n+1))))
