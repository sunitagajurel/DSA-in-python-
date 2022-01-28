#create stack
def createStack(): 
    stack = []
    return stack  

def isEmpty(): 
    if len(stack)==0:
        return True
#push into stack
def pushStack(stack,item): 
    return stack.append(item)

#pop item from stack 
def popStack(stack):
    if len(stack) == 0:
        return "stack is empty"
    
    p = stack.pop()
    return "popped item is {}".format(p)

#peek into stack
def peekStack(stack):
    top = stack[len(stack)-1]
    return ('the top of stack is {}'.format(top))

stack = createStack()
print(isEmpty())
pushStack(stack,1)
pushStack(stack,2)
pushStack(stack,3)
popStack(stack)
print(stack)
peekStack(stack)








