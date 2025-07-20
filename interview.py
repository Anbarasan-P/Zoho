from collections import deque

def ladderLength(beginWord, endWord, wordList):
    word_set = set(wordList)
    if endWord not in word_set:
        return 0

    queue = deque()
    queue.append((beginWord, 1))  # (current_word, level)

    while queue:
        word, level = queue.popleft()

        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                new_word = word[:i] + c + word[i+1:]

                if new_word == endWord:
                    return level + 1

                if new_word in word_set:
                    queue.append((new_word, level + 1))
                    word_set.remove(new_word)  # mark as visited

    return 0  # no transformation found


beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

print(ladderLength(beginWord, endWord, wordList))
# Output: 5

