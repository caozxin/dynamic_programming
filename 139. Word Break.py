## my original verions: however, it does not pass the time complexity. 

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        if not s:
            return False
        n = len(s)
        res = []
        final_res = False
        def dfs_backtrack(start_idx, path):
            if start_idx == n:
                res.append("".join(path))
                # print("res", res)
                if s in res:
                    final_res = True
                    return
                return
            get_edges = wordDict
            for edge in get_edges:
                if edge not in s[start_idx:]: # check if the edge is a prefix 
                    continue
                # print(edge, path)
                path.append(edge)
                dfs_backtrack(start_idx + len(edge), path)
                path.pop()

        dfs_backtrack(0, [])
        if s in res:
            return True
        else:
            return False
        # return final_res


### improved version using memoization:
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)
        memo = {}

        def dfs_backtrack(start_idx, path):
            if start_idx == n:
                return True  # valid segmentation
            
            if start_idx in memo:
                return memo[start_idx]

            for end_idx in range(start_idx + 1, n + 1):
                word = s[start_idx:end_idx]
                if word in word_set:
                    path.append(word)  # track current path (like yours)
                    if dfs_backtrack(end_idx, path):
                        memo[start_idx] = True
                        return True
                    path.pop()  # backtrack

            memo[start_idx] = False
            return False

        return dfs_backtrack(0, [])
