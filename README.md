### Memoization with Backtracking Template:
    class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int: # --> main function
        
        #Memoization Template with Backtracking:
        memo = {}

        def dfs_backtrack(start_idx):
            if is_leaf (start_idx):
                return result_value

            if start_idx in memo:
                return memo[start_idx]

            define result_value = ?

            for edge in get_edge(start_idx/end_idx):

                if not is_valid(edge):
                    continue

                if dfs_backtrack(start_idx/end_idx + len(edge), ...):
                    update result_value


            memo[start_idx] = result_value
            return result_value

        return dfs_backtrack(0)
