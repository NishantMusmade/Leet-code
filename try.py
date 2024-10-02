def valid(s):
    open_brackets = []
    for char in s:
        if char == '(' or char == '[' or char == '{':
            open_brackets.append(char)
        elif char == ')' or char == ']' or char == '}':
            if len(open_brackets) > 0:
                stack_top = open_brackets.pop()
            else:
                return False
            if stack_top == '(' and char != ')':
                return False
            elif stack_top == '[' and char != ']':
                return False
            elif stack_top == '{' and char != '}':
                return False
    
    if len(open_brackets) > 0:
        return False
    else:
        return True
                
s = ']'
result=valid(s)
print(result)