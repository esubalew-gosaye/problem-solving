# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, paths: str) -> str:
        stack = []
        for path in paths.split("/"):
            if path != "":
                if path == "..":
                    if stack:
                        stack.pop()
                elif path != ".":
                    stack.append(path)
        
        return "/" + "/".join(stack)