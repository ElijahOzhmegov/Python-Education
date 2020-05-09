from typing import List


class Solution:
    @staticmethod
    def checkStraightLine(coordinates: List[List[int]]) -> bool:
        first = coordinates[0]
        second = coordinates[1]

        try:
            k = (second[1] - first[1]) / (second[0] - first[0])
            b = first[1] - k * first[0]
        except ZeroDivisionError:
            return False

        # print(k, b)

        n = len(coordinates)

        for i in range(2, n):
            point = coordinates[i]
            # print(point[0], k * point[0] + b)
            if point[1] != k * point[0] + b: return False

        return True


if __name__ == '__main__':
    assert Solution.checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]) is False
    assert Solution.checkStraightLine([[-7,-3],[-7,-1],[-2,-2],[0,-8],[2,-2],[5,-6],[5,-5],[1,7]]) is False

