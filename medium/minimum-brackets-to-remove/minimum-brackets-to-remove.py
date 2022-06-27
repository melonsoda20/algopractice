class Solution:
    def minRemoveToMakeValid(s: str) -> str:
        bracket_queue = []
        splitted_s = list(s)

        for index, value in enumerate(splitted_s):
            print(value)
            if value == "(":
                bracket_queue.append(index)
            elif value == ")":
                if len(bracket_queue) == 0:
                    splitted_s[index] = ""
                else:
                    bracket_queue.pop()

        for index_data in bracket_queue:
            splitted_s[index_data] = ""

        return "".join(splitted_s)


print(Solution.minRemoveToMakeValid("lee(t(c)o)de)"))
