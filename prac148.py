#백준 19539 못품
import sys
N=int(sys.stdin.readline())
apple = list(map(int,sys.stdin.readline().split()))
apple_sum = sum(apple)
turn = apple_sum // 3

if apple_sum % 3 != 0:
    print('NO')
else:
    for a in apple:
        turn -= (a//2)
    if turn > 0:
        print('NO')
    else:
        print('YES')