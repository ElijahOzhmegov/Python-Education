from typing import List


class Solution:
    @staticmethod
    def majorityElement(nums: List[int]) -> int:
        from collections import Counter
        cc = Counter(nums)
        return cc.most_common(1)[0][0]


if __name__ == '__main__':
    assert 3 == Solution.majorityElement([3, 2, 3])
    assert 2 == Solution.majorityElement([2,2,1,1,1,2,2])

