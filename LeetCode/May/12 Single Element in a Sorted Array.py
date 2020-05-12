from typing import List


class Solution:
    @staticmethod
    def singleNonDuplicate(nums: List[int]) -> int:
        l, r = 0, len(nums)
        if r == 1: return nums[0]

        while r > l:
            m = (l + r) // 2
            m += m % 2
            if nums[m] == nums[(m + 1) % len(nums)]:
                l = m
            elif nums[m] == nums[m - 1]:
                r = m - 1
            else:
                return nums[m]


if __name__ == '__main__':
    nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
    assert Solution.singleNonDuplicate(nums) == 2

    nums = [1, 1, 2, 2, 3, 3, 5, 4, 4, 8, 8]
    assert Solution.singleNonDuplicate(nums) == 5

    nums = [1]
    assert Solution.singleNonDuplicate(nums) == 1

    nums = [1, 1, 2]
    assert Solution.singleNonDuplicate(nums) == 2

    nums = [1,2,2,3,3]
    assert Solution.singleNonDuplicate(nums) == 1
