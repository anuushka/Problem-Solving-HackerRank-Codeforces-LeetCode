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
