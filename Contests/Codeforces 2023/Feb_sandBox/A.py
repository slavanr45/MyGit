a = int(input())
print(*list(sum(map(int, input().split())) for _ in range(a)), sep='\n')