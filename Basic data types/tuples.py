'''
Input Format
The first line contains an integer, n , denoting the number of elements in the tuple.
The second line contains  space-separated integers describing the elements in tuple t.

Output Format
Print the result of hash(t).
'''

if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    tup = tuple(integer_list)
    print(hash(tup))
