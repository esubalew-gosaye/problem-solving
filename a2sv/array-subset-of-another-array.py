
def isSubset( a1, a2, n, m):
    
    
    for i in a2:
        if not i in a1:
            return "No"
        else:
            a1.remove(i)
    return "Yes"
