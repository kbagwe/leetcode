class Solution:
    def isValid(self, s: str) -> bool:
        # Stack for left symbols
        paranthesis = []
        # Loop for each character of the string
        for brackets in s:
            # If left symbol is encountered
            if brackets in ['(', '{', '[']:
                paranthesis.append(brackets)
            # If right symbol is encountered
            elif brackets == ')' and len(paranthesis) != 0 and paranthesis[-1] == '(':
                paranthesis.pop()
            elif brackets == '}' and len(paranthesis) != 0 and paranthesis[-1] == '{':
                paranthesis.pop()
            elif brackets == ']' and len(paranthesis) != 0 and paranthesis[-1] == '[':
                paranthesis.pop()
            # If none of the valid symbols is encountered
            else:
                return False
        return paranthesis == []
