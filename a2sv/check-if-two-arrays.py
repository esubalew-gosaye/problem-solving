class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,A,B,N):
        store_a = {}
        store_b = {}
        for a in A:
            if a in store_a:
                store_a[a]+=1
            else:
                store_a[a] = 1
        for a in B:
            if a in store_b:
                store_b[a]+=1
            else:
                store_b[a] = 1
        for i in store_a:
            if not(i in store_b and store_a[i] == store_b[i]):
                return False
        return True
