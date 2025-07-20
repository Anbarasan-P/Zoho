class Solution():
    def groupAnagrams(self, strs):
        anagram_map = {}

        for word in strs:
            sorted_word = ''.join(sorted(word))    # Sort the word 

            if sorted_word not in anagram_map:
                anagram_map[sorted_word] = []

            anagram_map[sorted_word].append(word)

        return list(anagram_map.values())


    

strs = ["eat","tea","tan","ate","nat","bat"]
sol = Solution()
print(sol.groupAnagrams(strs))