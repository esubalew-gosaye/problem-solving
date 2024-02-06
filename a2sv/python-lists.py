if __name__ == '__main__':
    loop = int(input())
    list_item = []
    for _ in range(loop):
        action = input().split()
        
        if action[0] == "insert":
            list_item.insert(int(action[1]), int(action[2]))
        elif action[0] == "pop":
            list_item.pop()
        elif action[0] == "reverse":
            list_item.reverse()
        elif action[0] == "sort":
            list_item.sort()
        elif action[0] == "append":
            list_item.append(int(action[1]))
        elif action[0] == "remove":
            list_item.remove(int(action[1]))
        elif action[0] == "print":
            print(list_item)
