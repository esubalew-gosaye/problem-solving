if __name__ == '__main__':
    n = int(input().strip())
    if n%2:
        print("Weird")
    elif n in [2, 4]:
        print("Not Weird")
    elif n in range(6, 21, 2):
        print("Weird")
    else:
        print("Not Weird")
