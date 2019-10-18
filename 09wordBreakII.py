"""
单词拆分 II
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。

说明：

分隔时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：

输入:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
输出:
[
  "cats and dog",
  "cat sand dog"
]
示例 2：

输入:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
输出:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
解释: 注意你可以重复使用字典中的单词。
示例 3：

输入:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
输出:
[]
"""


class Solution:
    """
    记忆化+dfs+剪枝，轻松超过95%+，详细注释见题解

    剪枝同样能大大减小空间复杂度，对aaaaaaaaaabaaaa那个用例不用特意优化
    """

    def wordBreak(self, s: str, wordDict: list) -> list:
        if not s or not wordDict:
            return []
        _len, wordDict = len(s), set(wordDict)
        _min = min(map(len, wordDict))
        _max = max(map(len, wordDict))

        def dfs(start):  # 返回s[start:]能由字典构成的所有句子
            if start not in memo:
                res = []
                # 剪枝
                for i in range(_min, min(_max, _len - start) + 1):
                    if s[start: start + i] in wordDict:
                        res.extend(list(map(lambda x: s[start: start + i] + ' ' + x, dfs(start + i))))
                memo[start] = res
            return memo[start]

        memo = {_len: ['']}
        # 去掉末尾空格
        return list(map(lambda x: x[:-1], dfs(0)))


if __name__ == '__main__':
    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    sol = Solution()
    res = sol.wordBreak(s, wordDict)
    for l in res:
        print(l)
