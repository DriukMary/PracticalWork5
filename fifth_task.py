# Read total pins (n) and throws count (k)
n, k = map(int, input("Enter n and k: ").split())

pins = ['I'] * n

for _ in range(k):
    m, h = map(int, input().split())
    for j in range(m - 1, h):
        pins[j] = '.'


print("".join(pins))
