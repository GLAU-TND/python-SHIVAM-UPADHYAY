n = int(input())
arr = input().split()
res = list(map(int,arr))
print(max([res.count(i) for i in res]))