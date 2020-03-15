class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_max = 0
        max_len = 0
        faced_characters = []

        for character in s:
            if character not in faced_characters:
                max_len += 1
                faced_characters.append(character)
            else:
                faced_characters = [character]
                max_max = max_len if max_len > max_max else max_max
                max_len = 1

        return max_len if max_len > max_max else max_max


if __name__ == '__main__':
    ss = Solution()
    # assert ss.lengthOfLongestSubstring('abcabcbb') == 3
    # assert ss.lengthOfLongestSubstring('bbbbb') == 1
    # assert ss.lengthOfLongestSubstring('pwwkew') == 3
    # assert ss.lengthOfLongestSubstring(' ') == 1
    assert ss.lengthOfLongestSubstring('dvdf') == 3
