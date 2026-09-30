n = int(input())
l = list(map(int, input().split()))
s = 0
for x in l:
    s += x
print(s)

#Short version:
n = int(input())
l = list(map(int, input().split()))
print(sum(l))

# Odd number count
n = int(input())
l = list(map(int, input().split()))
o = 0
for x in l:
    if x % 2 != 0:
        o += 1 
print(o)

# Multiple First Output
import sys
r = []
for i in range(5):
    r.append(str(i))
sys.stdout.write("\n".join(r))

#Multiple Test case:
import sys
input = sys.stdin.buffer.readline
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    print(sum(a))

#Even odd check in list:
import sys
input = sys.stdin.buffer.readline
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    cnt = 0
    for x in a:
        if x % 2 == 0:
            cnt += 1
    print(cnt)

# Average < list eliment 
import sys
input = sys.stdin.buffer.readline
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    cnt = 0
    for x in a:
        avg = sum(a)/n 
        if avg < x :
            cnt += 1
    print(cnt)

# Sliding Window
arr = [2,3,4,5,6,9]
t = 345
for i in range(len(arr)):
    for j in range(1, len(arr)):
        if arr[i] + arr[j] == t:
            print("found")
            break;  
else:
    print("Not found")


