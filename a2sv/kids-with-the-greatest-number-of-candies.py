class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
       
        max_candy = max(candies) # finding the greatest candy from the list

        return [True if candy + extraCandies >= max_candy else False for candy in candies ]

