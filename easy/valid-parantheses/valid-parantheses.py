class Solution:
    def isValid(s: str) -> bool:
        if len(s) == 0:
            return True

        params = {
            "[": "]",
            "{": "}",
            "(": ")"
        }

        stack = []

        for val in s:
            if val in params.keys():
                stack.append(val)
            else:
                if len(stack) > 0:
                    value_from_top_stack = params.get(stack.pop())
                    if value_from_top_stack != val:
                        return False
                else:
                    return False

        return len(stack) == 0


print(Solution.isValid("()"))
