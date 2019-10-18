"""
单词拆分
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：

拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：

输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
示例 2：

输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。
示例 3：

输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false
"""
from typing import List


class Solution:
    """
    动态规划，用dp数组来存储从第一个元素到当前元素组成的字符串是否满足要求，那么我们需要的就是dp[len(s)-1]

    对于第i个元素来说，dp[i]为真的条件是：（1）s[:i+1]在字典中，或（2）s[j+1:i+1]在字典中，且dp[j]为真

    """

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not wordDict:
            return False
        wordDict = set(wordDict)
        dp = [False for _ in range(len(s))]
        max_len = max(map(len, wordDict))
        min_len = min(map(len, wordDict))
        for i in range(min_len - 1, len(s)):
            if s[:i + 1] in wordDict:
                dp[i] = True
                continue
            for j in range(max(i - max_len, 0), max(i - min_len + 1, 0)):
                if dp[j] and s[j + 1:i + 1] in wordDict:
                    dp[i] = True
                    break
        return dp[len(s) - 1]


if __name__ == '__main__':
    s = "bb"
    wordDict = ["a", "b", "bbb", "bbbb"]
    sol = Solution()
    print(sol.wordBreak(s, wordDict))
