l = list(input("Enter string of parenthesis"))
class Parenthesis:
    a=10
    def Stack(self,l):
        stack = []
        for a in l:
            if (a=='(' or a=='{' or a=='['):
                stack.append(a)
            elif (a==')' or a=='}' or a==']'):
                if len(stack)==0:
                    print("Parenthesis not matched")
                    break
                x=self.Pop(a,stack)
                if(x==-1):
                    print("Parenthesis not matched")
                    break
        else:
            return 1
    def Pop(self,a,stack):
        if (chr(ord(a)-2)==stack[-1] or (a==')' and stack[-1]=='(')):
            stack.pop()
        else:
            return -1
pt = Parenthesis()
s=pt.Stack(l)
if s:
    print("Parenthesis Matched")