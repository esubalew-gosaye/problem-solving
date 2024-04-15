# Problem: Count Vowel Strings in Ranges - https://leetcode.com/problems/count-vowel-strings-in-ranges/

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefix_sum = [0]
        vowels = {'a', 'e', 'i', 'o', 'u'}

        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                prefix_sum.append(prefix_sum[-1] + 1)
            else:
                prefix_sum.append(prefix_sum[-1])

        return [prefix_sum[query[1] + 1] - prefix_sum[query[0]] for query in queries]