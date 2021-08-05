def isValid(self, s: str) -> bool:
    # maps closing bracket to opening
    bracketMap = {")": "(", "]": "[", "}": "{"}

    # stack to track unclosed brackets
    bracketStack = []

    # iterate through string
    for ch in s:
        if ch in bracketMap:
            # got a closing bracket - first check there is at least one unclosed opening bracket
            if not bracketStack:
                return False

            # then check most recent unclosed opening bracket matches
            unclosed = bracketStack.pop()
            if unclosed != bracketMap[ch]:
                return False
        else:
            # got an opening bracket, so push it to the stack
            bracketStack.append(ch)

    # only valid if no unclosed opening brackets
    return len(bracketStack) == 0
