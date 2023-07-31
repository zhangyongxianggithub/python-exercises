"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
"""
tring = input('input string: ')
max = 0
res = 0
start = 0
end = 0
for s in string:
    if not s in string[start:end]:
        end += 1
        res += 1
        if res > max:
            max = res
    else:
        start += 1
