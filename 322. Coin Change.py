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

            if curr_sum >= target:
                if curr_sum ==  target and min_path[0] >= len(path):
                    min_path[0]  = len(path)
                return min_path[0]

            for edge in coins:
                path.append(edge)
                curr_sum += edge

                dfs_backtrack(start_idx + 1, path[:], min_path, sum(path[:]))

                path.pop()

        dfs_backtrack(0, [], min_path, 0)

        if min_path[0] != float('inf'):
            return min_path[0] 
        else:
            return -1
