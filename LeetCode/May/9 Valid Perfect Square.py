class Solution:
    @staticmethod
    def isPerfectSquare(num: int) -> bool:
        if num == 1: return True

        def update_middle():
            previous = mid
            mm = (l + r) // 2
            if mm == previous:
                return mm + 1, (mm + 1) ** 2
            return mm, mm ** 2

        l = 1
        r = num // 2 + 1

        mid = -1
        mid, squared_mid = update_middle()

        while r - l > 1:
            if squared_mid == num: return True
            if squared_mid > num: r = mid
            else: l = mid

            mid, squared_mid = update_middle()

        return False


if __name__ == '__main__':
    assert Solution.isPerfectSquare(1) is True
    assert Solution.isPerfectSquare(16) is True
    assert Solution.isPerfectSquare(14) is False

    assert Solution.isPerfectSquare(5) is False
