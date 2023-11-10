a = int(input())
b = int(input())
res = (1 << a) - 1 << b
print(f"result: {bin(res)}")