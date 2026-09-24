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