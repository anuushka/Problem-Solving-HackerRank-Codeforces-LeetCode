'''
Function Description:

You are given a string S and width w.
Your task is to wrap the string into a paragraph of width w.

Complete the wrap function in the editor below.
wrap has the following parameters:
string string: a long string
int max_width: the width to wrap to

Input Format
The first line contains a string, string
The second line contains the width, max_width

Constraints:
 0 < len(string) < 1000
 0 < max_width < len(string)

Returns
string: a single string with newline characters ('\n') where the breaks should be

Input:
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4

Output: 
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
'''

#Method 1 "Math way"
import textwrap

def wrap(string, max_width):
    wrapped_str = ""
    for i in range(len(string)):
        if (i + 1) % max_width == 0: 
            wrapped_str += string[i - (max_width - 1):i+1] + '\n'
        elif (i % max_width == 0) and len(string) - i < max_width:
            wrapped_str += string[i:len(string)] + '\n'
    return wrapped_str

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

#Method 2 Stepped Slicing by max_width
import textwrap

def wrap(string, max_width):
    wrapped_str = ""
    for i in range(0,len(string),max_width):
        wrapped_str += string[i : i + max_width] + '\n'
    return wrapped_str

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

#Method 3 library built-in function
import textwrap

def wrap(string, max_width):
    wrapped_str = textwrap.fill(string, max_width)
    return wrapped_str

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
