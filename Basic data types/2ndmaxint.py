'''
Given list is [2,3,5,6,6]. The maximum score is 6, second maximum is 5. Hence, we print 5 as the runner-up score.
'''


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    a = sorted(list(set(arr)), reverse='True')
    print(a[1])
