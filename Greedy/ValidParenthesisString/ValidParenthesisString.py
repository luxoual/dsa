class Solution:
    def checkValidString(self, s: str) -> bool:
        # First thoughts makes me think of the other
        # valid parenthesis question, where we use a stack
        # we push onto the stack, when we see a '('
        # when we see a ')' we pop from the stack

        # The difference here though is that since * can be anything
        # we could technically keep track of how many we have
        # and make hte best move that we can from there

        # A very clear testcase is that, if theres no open
        # parenthesis in the stack so far, and we get a closing
        # then our secondary check is if we have any *

        # Hint: Originally, we said that we can return True
        # if we have more wildcards than the size of our stack
        # but that isn't necessarily true because a wildcard isn't
        # helpful unless it comes after a opener, so we need some way
        # to keep track of the indices of the wildcards, so we know
        # when they come after an opener.

        wild = []
        stack = []
        n = len(s)
        for i in range(n):
            char = s[i]
            if char == '(': stack.append(i)
            elif char == ')':
                if not stack:
                    if not wild: return False
                    wild.pop(-1)
                else:
                    stack.pop(-1)
            elif char == '*': wild.append(i)

        while stack and wild:
            if wild[-1] > stack[-1]:
                # We can close an opener
                stack.pop(-1)
                wild.pop(-1)
            else: return False
    
        return True if not stack else False
