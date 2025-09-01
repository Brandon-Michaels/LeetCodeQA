# Problem Summary
# Task: implement prefix tree
# 3 operations:
# insert => insert word into prefix tree
# search => returns boolean if word in tree
# startsWith => returns boolean if prefix in tree

# Non-Optimal Approach:
# Hash Set
# Store all words in a hash set, check startsWith by scanning
# all words and testing => word.startsWith(prefix)
# O(N * L), n is nodes in tree, L is length of input string

# Optimal Approach
# Use a Trie node with up to 26 children (26 chars in alphabet)
# and an is_word flag
# Time-Complexity: O(L), where L is length of string
# Space-Complexity: O(t), where t is total characters inserted

class TrieNode:
    def __init__(self):
        # children maps char -> TrieNode
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        # root represents empty prefix
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # traverse from root, creating nodes for each char
        # cat => c, ca, cat
        node = self.root
        
        for c in word:
            # create next node if missing
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        
        # after a node fully traversed
        # then we know it's full presence
        node.is_word = True

    def search(self, word: str) -> bool:
        # walk through the tree
        # determine if char is in PrefixTree while walking traversing
        node = self.root
        for c in word:
            # return early (boolean) if path missing
            if c not in node.children:
                return False
            node = node.children[c]
        
        # if full flag word set => return True, else False
        return node.is_word

    def startsWith(self, prefix: str) -> bool:
        # same as search
        # but this time don't need to see whole word
        # when prefix is seen, then return True, else False
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True
   
