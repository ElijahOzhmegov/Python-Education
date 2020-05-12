from typing import List


class Solution:
    @staticmethod
    def singleNonDuplicate(nums: List[int]) -> int:
        l, r = 0, len(nums)

        while r > l:
            m = (l + r) // 2
            m -= m % 2
            if nums[m] == nums[m + 1]:
                l = m
            elif nums[m] == nums[m - 1]:
                r = m
            else:
                return nums[m]


if __name__ == '__main__':
    nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
    res = 2

    assert Solution.singleNonDuplicate(nums) == res

    nums = [1, 1, 2, 2, 3, 3, 5, 4, 4, 8, 8]
    assert Solution.singleNonDuplicate(nums) == 5
