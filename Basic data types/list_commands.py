'''
Consider a list (list = []). You can perform the following commands:
insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.

Input Format
The first line contains an integer,n, denoting the number of commands.
Each line i of the n subsequent lines contains one of the commands described above.

Output Format
For each command of type print, print the list on a new line.'''

if __name__ == '__main__':
    N = int(input())
    arr = []
    for _ in range(N):
        cmd_name, *args = input().split()
        args = list(map(int, args))
        
        if cmd_name == "insert":
            arr.insert(args[0], args[1])
        elif cmd_name == "print":
            print(arr)
        elif cmd_name == "remove": 
            arr.remove(args[0])
        elif cmd_name == "append":
            arr.append(args[0])
        elif cmd_name == "sort":
            arr.sort()
        elif cmd_name == "pop":
            arr.pop()
        elif cmd_name == "reverse":
            arr.reverse()
            
        
        
        
