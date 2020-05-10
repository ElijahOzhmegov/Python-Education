from typing import List


class Solution:
    @staticmethod
    def findJudge(N: int, trust: List[List[int]]) -> int:
        src = [0] * N
        dst = [0] * N

        for src2dst in trust:
            src[src2dst[0] - 1] += 1
            dst[src2dst[1] - 1] += 1

        for i in range(N):
            if dst[i] == N - 1 and src[i] == 0:
                return i + 1

        return -1


if __name__ == '__main__':
    N = 3; trust = [[1, 3], [2, 3], [3, 1]]
    assert Solution.findJudge(N, trust) == -1

    N = 2; trust = [[1, 2]]
    assert Solution.findJudge(N, trust) == 2

    N = 3; trust = [[1,3],[2,3]]
    assert Solution.findJudge(N, trust) == 3

    N = 3; trust = [[1,3],[2,3],[3,1]]
    assert Solution.findJudge(N, trust) == -1

    N = 3; trust = [[1, 2], [2, 3]]
    assert Solution.findJudge(N, trust) == -1

    N = 4; trust = [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]
    assert Solution.findJudge(N, trust) == 3

    N = 1; trust = []
    assert Solution.findJudge(N, trust) == 1

