'''
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回 s 所有可能的分割方案。

示例:

输入: "aab"
输出:
[
    ["aa","b"],
    ["a","a","b"]
]
'''


class Solution:
    def __init__(self):
        self.s = None
        self.PMatrix = None
        self.res = []

    def _init_palindrome_matrix(self):
        s = self.s
        length = len(s)

        dp = [[0 for _ in range(length)] for _ in range(length)]
        for i in range(length):
            dp[i][i] = 1
        for i in range(length - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = 1
        for k in range(length - 2):
            for i in range(length - k - 2):
                if dp[i + 1][i + k + 1] == 1 and s[i] == s[i + k + 2]:
                    dp[i][i + k + 2] = 1

        self.PMatrix = dp

    # 深度优先搜索
    def _find(self, start_index: int, splits: list):
        if start_index == len(self.s):
            self._add_result(splits)
            return
        for i in range(start_index, len(self.s)):
            if not self.PMatrix[start_index][i]:
                continue
            splits.append(i)
            self._find(i + 1, splits)
            splits.pop()

    def _add_result(self, splits):
        partitions = []
        start_index = 0
        for i in range(len(splits)):
            partitions.append(self.s[start_index: splits[i] + 1])
            start_index = splits[i] + 1
        self.res.append(partitions)

    def partition(self, s):
        self.s = s
        self._init_palindrome_matrix()
        self._find(0, [])
        return self.res


if __name__ == '__main__':
    solution = Solution()
    res = solution.partition('a')
    for l in res:
        print(l)
