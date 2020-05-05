class Solution:
    @staticmethod
    def firstUniqChar(s: str) -> int:
        if len(s) <= 0: return -1

        d = dict()
        for char in s:
            if char in d:
                d[char] += 1
            else:
                d[char] = 1
        the_least = sorted(d.items(), key=lambda item: item[1])[0]
        if the_least[1] > 1: return -1
        return s.find(the_least[0])


if __name__ == '__main__':
    s, a = "leetcode", 0
    assert a == Solution.firstUniqChar(s)

    s, a = "loveleetcode", 2
    assert a == Solution.firstUniqChar(s)

    s, a = "", -1
    assert a == Solution.firstUniqChar(s)

    s, a = "cc", -1
    assert a == Solution.firstUniqChar(s)
