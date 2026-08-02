class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        top = -1
        operands = ("+","-","*","/")
        for i in tokens:
            # print(stack)
            if i not in operands:
                stack.append(int(i))
                top+=1
            elif i == "+":
                a = stack.pop()
                b = stack.pop()
                top-=1
                stack.append(a+b)
            elif i == "-":
                a = stack.pop()
                b = stack.pop()
                top-=1
                stack.append(b-a)
            elif i == "*":
                a = stack.pop()
                b = stack.pop()
                top-=1
                stack.append(a*b)
            else:
                a = stack.pop()
                b = stack.pop()
                top-=1
                stack.append(int(b/a))
        return stack[0]