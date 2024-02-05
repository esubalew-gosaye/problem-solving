class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        value = 0
        for operation in operations:
            if operation[:2] == "--" or operation[-2:] == "--":
                value -= 1
            else:
                value += 1
        return value
