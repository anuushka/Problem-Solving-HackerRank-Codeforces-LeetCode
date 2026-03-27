'''
Example
records = [["chi", 20.0], ["alpha", 50.0], ["beta", 50.0]]
The ordered list of scores is [20.0, 50.0], so the second lowest score is 50.0. 
There are two students with that score: ["beta","alpha"]. 
Ordered alphabetically, the names are printed as: 
alpha
beta

Input Format
The first line contains an integer, N , the number of students.
The 2N subsequent lines describe each student over 2 lines.
- The first line contains a student's name.
- The second line contains their grade.

Constraints
2 <= N <= 5
There will always be one or more students having the second lowest grade.
Output Format

Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.
'''
if __name__ == '__main__':
    records = []
    low_students = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])

scores = sorted(list(set(r[1] for r in records)))
low_score = scores[1]

for r in records:
    if r[1] == low_score:
        low_students.append(r[0])
        low_students.sort()

for name in low_students:
    print(name)
