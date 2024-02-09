n = int(input())
store = dict()
for _ in range(n):
    key, value = input().split()
    store[key] = value
while True:
    try:
        key = input()
        val = store.get(key)
        if val is None:
            print("Not found")
        else:
            print(f"{key}={val}")
    except:
        break
