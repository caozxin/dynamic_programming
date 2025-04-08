class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 0

        if s[0] == '0': # any leading zero is invalid
            return 0
