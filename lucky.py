t = int(input())
for i in range(t):
    s = list(map(int, input()))
    if sum(s[: len(s) // 2]) == sum(s[len(s) // 2 :]):
        print("YES")
    else:
        print("NO")
