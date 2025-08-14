size = 10
arr = []
for i in range(size):
    arr.append(i * 2)
print(arr)

size = 10
arr = [ i * 2 for i in range(size)]
print(arr)

# 조건문으로 필터링링
size = 10
arr = [n for n in range(1, 11) if n % 2 == 0]
print(arr)