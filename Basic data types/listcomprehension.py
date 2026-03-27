import itertools
'''
Input: 
x
y
z
n

Output:
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
'''
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    newlist = [[i,j,k] for i in range(x+1) for j in range(y+1)
    for k in range(z+1) if i + j + k != n]
    print(newlist)
    
