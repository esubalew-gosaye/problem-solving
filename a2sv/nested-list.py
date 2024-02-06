if __name__ == '__main__':
    list_of_mark = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list_of_mark+=[(name, score)]
        
    list_of_mark.sort(key=lambda x:x[-1])

    index = 0
    for each in list_of_mark:
        if each[1] == list_of_mark[0][1]:
            index += 1 

    ##print(index, list_of_mark)
    list_of_second = [list_of_mark[index]]
    for i in list_of_mark[index+1:]:
        if list_of_second[0][-1] == i[-1]:
            list_of_second.append(i)

    for j in sorted(list_of_second, key=lambda x:x[0]):
        print(j[0])
