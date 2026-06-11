class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        opened = []
        for elt in s:
            print(elt)
            if elt in {"(", "[", "{"}:
                opened.append(elt)
            else:
                if opened == []:
                    return False
                last_open = opened[-1]
                if pairs[last_open] == elt:
                    opened.pop(-1)
                else:
                    return False
        if len(opened) == 0:
            return True
        return False
