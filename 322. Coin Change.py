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
        # res=[]
        min_path = [float('inf')]

        def dfs_backtrack(start_idx, path, min_path):
            # print("path", path)
            if sum(path) >= target:
                # print("path", path)
                print("     reach leaf", path)
                if sum(path) ==  target and min_path[0] >= len(path):

                    min_path[0]  = len(path)
                    print("min_path ", min_path)
                    # exit()
                # res.append(path)

                return min_path[0]


            for edge in coins:
                path.append(edge)

                dfs_backtrack(start_idx + 1, path[:], min_path)
                # print("path", path)
                path.pop()

        dfs_backtrack(0, [], min_path)
        print(min_path)
        if min_path[0] != float('inf'):
            return min_path[0] 
        else:
            return -1
