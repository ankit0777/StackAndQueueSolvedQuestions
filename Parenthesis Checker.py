# Given an expression string exp. Examine whether the pairs and the orders of “{“,”}”,”(“,”)”,”[“,”]” are correct in exp.
# For example, the program should print 'balanced' for exp = “[()]{}{[()()]()}” and 'not balanced' for exp = “[(])”
#code
t=int(input())
while(t):
    s=input()
    l1=[]
    for i in s:
        l1.append(i)
    flag=1
    l2=[]
    for i in range(len(l1)):
        if(l1[i]=='{' or l1[i]=='(' or l1[i]=='['):
            l2.append(l1[i])
        else:
            if(len(l2)==0):
                flag=0
                break
            if(l1[i]=='}'):
                p=l2.pop()
                if(p != '{'):
                    flag=0
                    break
            if(l1[i]==')'):
                p=l2.pop()
                if(p != '('):
                    flag=0
                    break
            if(l1[i]==']'):
                p=l2.pop()
                if(p != '['):
                    flag=0
                    break
    if(flag==0):
        print("not balanced")
    elif(len(l2) !=0):
        print("not balanced")
    else:
        print('balanced')
    t=t-1
                
