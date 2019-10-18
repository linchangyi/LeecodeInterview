"""
 字符串中的第一个唯一字符
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

案例:

s = "leetcode"
返回 0.

s = "loveleetcode",
返回 2.
注意事项：您可以假定该字符串只包含小写字母。
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        sets = set(s)
        counts = {}
        for ch in sets:
            counts[ch] = s.count(ch)
        for i in range(len(s)):
            if counts[s[i]] == 1:
                return i
        return -1

    def firstUniqChar2(self, s: str) -> int:
        _min = len(s)
        for c in 'abcdefghijklmnopqrstuvwxyz':
            i = s.find(c)
            if i == -1:
                continue
            if i == s.rfind(c):
                _min = min(_min, i)

        return _min if _min != len(s) else -1
