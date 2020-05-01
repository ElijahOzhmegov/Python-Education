def isBadVersion(version: int) -> bool:
    return True if version >= number else False


class Solution:
    @staticmethod
    def firstBadVersion(n: int) -> int:
        """
        :type n: int
        :rtype: int
        """
        if isBadVersion(1): return 1

        left = 1
        right = n

        while right - left > 1:
            middle = (left + right) // 2

            if isBadVersion(middle):
                right = middle
            else:
                left = middle

        return right


if __name__ == '__main__':
    for number in range(1, 1000):
        for j in range(number, 1000):
            assert number == Solution.firstBadVersion(j)











