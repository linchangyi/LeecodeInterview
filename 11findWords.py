"""
单词搜索 II
给定一个二维网格 board 和一个字典中的单词列表 words，找出所有同时在二维网格和字典中出现的单词。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。

示例:

输入:
words = ["oath","pea","eat","rain"] and board =
[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

输出: ["eat","oath"]
说明:
你可以假设所有输入都由小写字母 a-z 组成。

提示:

你需要优化回溯算法以通过更大数据量的测试。你能否早点停止回溯？
如果当前单词不存在于所有单词的前缀中，则可以立即停止回溯。什么样的数据结构可以有效地执行这样的操作？散列表是否可行？为什么？ 前缀树如何？如果你想学习如何实现一个基本的前缀树，请先查看这个问题： 实现Trie（前缀树）。
"""
from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        dx = ((0, 1), (0, -1), (1, 0), (-1, 0))
        w, h = len(board[0]), len(board)
        trie = Trie()
        for word in words:
            trie.insert(word)

        result = set()

        visited = [[False for _ in range(w)] for _ in range(h)]

        def dfs(i, j, tree, path):
            if board[i][j] not in tree:
                return
            path += board[i][j]
            visited[i][j] = True
            tree = tree[board[i][j]]
            # 找到
            if '#' in tree:
                result.add(path)
            for d in dx:
                xi, xj = i + d[0], j + d[1]
                if 0 <= xi < h and 0 <= xj < w and not visited[xi][xj]:
                    dfs(xi, xj, tree, path)
            # 还原
            visited[i][j] = False

        for i in range(h):
            for j in range(w):
                dfs(i, j, trie.root, '')

        return result


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        tree = self.root
        for w in word:
            if w not in tree:
                tree[w] = {}
            tree = tree[w]
        # 结束标志
        tree['#'] = '#'


if __name__ == '__main__':
    words = ["oath", "pea", "eat", "rain"]
    board = [
        ['o', 'a', 'a', 'n'],
        ['e', 't', 'a', 'e'],
        ['i', 'h', 'k', 'r'],
        ['i', 'f', 'l', 'v']
    ]
    sol = Solution()
    print(sol.findWords(board, words))
