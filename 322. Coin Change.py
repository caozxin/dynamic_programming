### my not working version:
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int: # --> main function
        if amount == 0:
            return 0

        if not coins:
            return -1

        #Memoization Template with Backtracking:
        memo = {}
        target = amount
        n = len(coins)

        min_path = [float('inf')]

        def dfs_backtrack(start_idx, path, min_path, curr_sum):
            # print(path)

            if curr_sum >= target:
                print("leaf", path)
                return min_path[0]

            if start_idx in memo:
                print("I am here", start_idx, memo[start_idx])
                
                return memo[start_idx]

            for edge in coins:
                if edge > target:
                    continue

                path.append(edge)
                curr_sum += edge

                if dfs_backtrack(start_idx + 1, path[:], min_path, sum(path[:])):
                    if curr_sum ==  target and min_path[0] >= len(path):
                        print("here", "min_path", min_path[0])
                        min_path[0]  = len(path)
                        # memo[start_idx] = min_path[0]
                path.pop()

            memo[start_idx] = min_path[0]


        dfs_backtrack(0, [], min_path, 0)

        if min_path[0] != float('inf'):
            return min_path[0] 
        else:
            return -1
### improved version using backtracking with memoization:
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(curr_sum):
            if curr_sum == amount:
                return 0
            if curr_sum > amount:
                return float('inf')
            if curr_sum in memo:
                return memo[curr_sum]

            min_coins = float('inf')
            for coin in coins:
                res = dfs(curr_sum + coin)
                if res != float('inf'):
                    min_coins = min(min_coins, res + 1)

            memo[curr_sum] = min_coins
            return min_coins

        result = dfs(0)
        return result if result != float('inf') else -1
