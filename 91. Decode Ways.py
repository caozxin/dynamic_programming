class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 0

        if s[0] == '0': # any leading zero is invalid
            return 0

        memo: Dict[int, int] = {}

        def dfs(start_index: int):
            if start_index in memo:
                return memo[start_index]
            if start_index == len(s):
                return 1

            ways = 0
            # can't decode string with leading 0
            if s[start_index] == "0":
                return ways
            # decode one digit
            ways += dfs(start_index + 1)
            # decode two digits
            if 10 <= int(s[start_index : start_index + 2]) <= 26:
                ways += dfs(start_index + 2)

            memo[start_index] = ways
            return ways

        return dfs(0)
