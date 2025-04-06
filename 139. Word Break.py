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
                return memo[start_idx] # Return cached result.

            for end_idx in range(start_idx + 1, n + 1):
                word = s[start_idx:end_idx] # word is a prefix of s. 
                if word in word_set:
                    path.append(word)  # track current path (like yours)
                    if dfs_backtrack(end_idx, path): # end_idx = start_idx + len(edge)
                        memo[start_idx] = True # # we can successfully break from this index to the end
                        return True
                    path.pop()  # backtrack

            memo[start_idx] = False  # we tried all possible paths from here and none worked
            return False

        return dfs_backtrack(0, [])
# memo example:s = "applepenapple" and wordDict = ["apple", "pen"].


        memo = {
        0: True,    # applepenapple is breakable
        5: True,    # penapple is breakable
        8: True     # apple is breakable
        }

### BEST version using memoization:
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return False

        word_set = set(wordDict)
        n = len(s)
        memo = {}
        res = []

        def dfs_backtrack(start_idx, path):
            if start_idx == n:
                joined = "".join(path)
                if joined == s:
                    res.append(joined)
                    return True
                return False

            if start_idx in memo:
                return memo[start_idx]

            for edge in word_set:
                if not s.startswith(edge, start_idx):
                    continue
                path.append(edge)
                if dfs_backtrack(start_idx + len(edge), path):
                    memo[start_idx] = True
                    return True
                path.pop()

            memo[start_idx] = False
            return False

        return dfs_backtrack(0, [])


### Another BEST version using memoization:
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return False

        word_set = set(wordDict)
        n = len(s)
        memo = {}
        res = []

        def dfs_backtrack(start_idx, path):
            #path has no use here. 
            if start_idx == n:
                return True
                # joined = "".join(path)
                # if joined == s:
                #     res.append(joined)
                #     return True
                # # return 

            if start_idx in memo:
                return memo[start_idx] # memo[start_idx] = "True/False". 

            for edge in word_set:
                if not s.startswith(edge, start_idx): # this is to check if the edge is a prefix of s, which means if edge == s[start_idx:]. 
                    continue
                # path.append(edge)
                if dfs_backtrack(start_idx + len(edge), path):
                    memo[start_idx] = True # if we go through everthing and it checks out, we should update memo[start_idx] = True and return True
                    return True
                # path.pop()

            memo[start_idx] = False
            return False

        return dfs_backtrack(0, [])
