def get_opening_bracket(symbol):
    if symbol == '}':
        return '{'
    elif symbol == ']':
        return '['
    else:
        return '('


def is_matched(expression):
    stack = []
    for symbol in expression:
        if symbol == '{' or symbol == '[' or symbol == '(':
            stack.append(symbol)
        else:
            if (len(stack) == 0):
                return False
            top_symbol = stack.pop()
            if top_symbol != get_opening_bracket(symbol):
                return False
    if len(stack) > 0 :
        return False
    else:
        return True


t = int(raw_input().strip())
for a0 in xrange(t):
    expression = raw_input().strip()
    if is_matched(expression) == True:
        print "YES"
    else:
        print "NO"

