class Solution():
    def lengthOfLongestSubstring(self, s):
        seen = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            max_len = max(max_len, right-left+1)
        return max_len
        # char_index = {}
        # start = 0
        # max_length = 0

        # for end in range(len(s)):
        #     if s[end] in char_index and char_index[s[end]] >=start:
        #         start = char_index[s[end]] + 1

        #     char_index[s[end]] = end
        #     max_length = max(max_length, end - start + 1)

        # return max_length
    


Sol = Solution()
print(Sol.lengthOfLongestSubstring("abcabcbb"))
print(Sol.lengthOfLongestSubstring("bbbbb"))
print(Sol.lengthOfLongestSubstring("pwwkew"))