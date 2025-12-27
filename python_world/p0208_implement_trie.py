from __future__ import annotations


class TrieNode:
    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.word = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for letter in word:
            node = node.children.setdefault(letter, TrieNode())
        node.word = True

    def search(self, word: str) -> bool:
        node = self._find(word)
        return bool(node and node.word)

    def startsWith(self, prefix: str) -> bool:
        return self._find(prefix) is not None

    def _find(self, text: str) -> TrieNode | None:
        node = self.root
        for letter in text:
            if letter not in node.children:
                return None
            node = node.children[letter]
        return node
