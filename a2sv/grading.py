def gradingStudents(grades):
    ls = []
    for g in grades:
        if g < 38:
            ls+=[g]
        else:
            ind = g//5
            if (ind+1)*5 - g < 3:
                ls+=[(ind+1)*5]
            else:
                ls+=[g]
    return ls
