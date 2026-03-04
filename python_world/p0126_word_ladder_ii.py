from collections import defaultdict


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
        unused = set(wordList)
        if endWord not in unused:
            return []
        parents: dict[str, set[str]] = defaultdict(set)
        level = {beginWord}
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        while level and endWord not in level:
            unused -= level
            next_level: set[str] = set()
            for word in level:
                for index, old in enumerate(word):
                    for letter in alphabet:
                        if letter == old:
                            continue
                        candidate = word[:index] + letter + word[index + 1 :]
                        if candidate in unused:
                            next_level.add(candidate)
                            parents[candidate].add(word)
            level = next_level
        if endWord not in level:
            return []
        result: list[list[str]] = []

        def build(word: str, path: list[str]) -> None:
            if word == beginWord:
                result.append(path[::-1])
                return
            for parent in parents[word]:
                build(parent, path + [parent])

        build(endWord, [endWord])
        return result

