class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        faced_characters = {}
        max_max = 0

        n = len(s)
        for i in range(n):
            if s[i] in faced_characters:
                max_max = len(faced_characters) if len(faced_characters) > max_max else max_max
                marker = faced_characters[s[i]]
                for faced_character in sorted(faced_characters.items(), key=lambda kv: kv[1]):
                    if faced_character[1] <= marker:
                        faced_characters.pop(faced_character[0])
                    else:
                        break

                faced_characters[s[i]] = i
            else:
                faced_characters[s[i]] = i

        return len(faced_characters) if len(faced_characters) > max_max else max_max



if __name__ == '__main__':
    ss = Solution()
    assert ss.lengthOfLongestSubstring('cdd') == 2
    assert ss.lengthOfLongestSubstring('abcabcbb') == 3
    assert ss.lengthOfLongestSubstring('bbbbb') == 1
    assert ss.lengthOfLongestSubstring('pwwkew') == 3
    assert ss.lengthOfLongestSubstring(' ') == 1
    assert ss.lengthOfLongestSubstring('dvdf') == 3
    assert ss.lengthOfLongestSubstring('bbtablud') == 6
