from typing import List


class Solution:
    @staticmethod
    def findJudge(N: int, trust: List[List[int]]) -> int:
        if N == 1: return 1
        con_dict = dict()  # [from me, to me]

        def check_n_expand(key):
            if key not in con_dict:
                con_dict[key] = [0, 0]

        for i in range(len(trust)):
            con = trust[i]

            check_n_expand(con[0])
            check_n_expand(con[1])

            con_dict[con[0]][0] += 1
            con_dict[con[1]][1] += 1

        ordered_con_list = sorted(con_dict.items(), key=lambda kvv: kvv[1][1])
        desired = ordered_con_list[-1]

        diff = desired[1][1] - desired[1][0] + 1

        return desired[0] if diff == N else -1


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

