class Solution():
    def justifyFull(self, words, maxWidth):
        result = []
        i = 0
        n = len(words)


        while i < n:
            len_line = len(words[i])
            j= i + 1

            while j < n and len_line + len(words[j]) + (j-1) <= maxWidth:
                len_line += len(words[j])
                j +=1

            line = ''
            num_words = j - i
            totalSpaces = maxWidth - len_line

            if j == n or num_words == 1:
                line = ' '.join(words[i:j])
                line += ' ' * (maxWidth - len(line))

            else:
                space_slots = num_words - 1
                even_spaces = totalSpaces // space_slots
                extra_spaces =totalSpaces % space_slots

                for k in range(i, j - 1):
                    line += words[k]
                    line += ''*(even_spaces + (1 if k-i < extra_spaces else 0))

                line += words[j-1]

            result.append(line)
            i = j

        return result
    

sol = Solution()

words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16

result = sol.justifyFull(words, maxWidth)
for line in result:
    print(f'"{line}"')
