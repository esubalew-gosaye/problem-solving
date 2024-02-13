class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        value = len(list1) + len(list2)
        elememnt = []

        # looping through the list store commons index and value as tuple into elememnt
        for i in range(len(list1)):
            if list1[i] in list2:
                ind = list2.index(list1[i])
                elememnt.append((i+ind, list1[i]))

        # Sort the element based on the index
        elememnt.sort()
        first_min = [elememnt[0][1]] # store first minimum index common

        #Search if there is another minimum index common
        for i in range(1, len(elememnt)):
            if elememnt[0][0] == elememnt[i][0]:
                first_min += [elememnt[i][1]]
        return first_min
