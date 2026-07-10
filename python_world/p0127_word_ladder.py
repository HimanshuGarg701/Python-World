from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        unused = set(wordList)
        if endWord not in unused:
            return 0
        queue = deque([(beginWord, 1)])
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        while queue:
            word, distance = queue.popleft()
            if word == endWord:
                return distance
            for index, old in enumerate(word):
                for letter in alphabet:
                    if letter == old:
                        continue
                    candidate = word[:index] + letter + word[index + 1 :]
                    if candidate in unused:
                        unused.remove(candidate)
                        queue.append((candidate, distance + 1))
        return 0

