class Solution:
    @staticmethod
    def numJewelsInStones(J: str, S: str) -> int:
        return sum([1 for s in S if s in J])


if __name__ == '__main__':
    assert 3 == Solution.numJewelsInStones("aA", "aAAbbbb")
    assert 0 == Solution.numJewelsInStones("z", "ZZ")
    assert 0 == Solution.numJewelsInStones("", "")
