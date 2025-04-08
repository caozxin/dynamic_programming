## default solution:

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

### solution using backtracking technique:
from typing import Dict

class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        memo: Dict[int, int] = {}

        def if_valid(edge: str) -> bool:
            if len(edge) == 1:
                return edge != '0'  # Single digit valid if not '0'
            if len(edge) == 2:
                return 10 <= int(edge) <= 26  # Two-digit numbers must be in range
            return False

        def dfs_backtrack(start_idx: int) -> int:
            if start_idx in memo:
                return memo[start_idx]

            if start_idx == len(s):
                return 1  # One valid way if we've reached the end

            total_ways = 0

            # Try 1-digit and 2-digit cuts
            for length in [1, 2]:
                end_idx = start_idx + length
                if end_idx <= len(s):
                    edge = s[start_idx:end_idx]
                    if if_valid(edge):
                        total_ways += dfs_backtrack(end_idx)

            memo[start_idx] = total_ways
            return total_ways

        return dfs_backtrack(0)

### Best Version:
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]

            if i == len(s):
                return 1  # Successfully reached the end

            if s[i] == '0':
                return 0  # Can't decode a standalone zero

            # Decode one digit
            res = dfs(i + 1)

            # Decode two digits if it's a valid number (10 to 26)
            if i + 1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
                res += dfs(i + 2)

            memo[i] = res
            return res

        return dfs(0)
