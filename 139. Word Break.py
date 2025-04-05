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
