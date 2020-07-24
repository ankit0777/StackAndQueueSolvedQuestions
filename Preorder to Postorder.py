# Given an array arr[] of N nodes representing preorder traversal of BST. The task is to print its postorder traversal.
def postorder(l1,l2):
    if(l1[0] in l2):
        i=l2.index(l1[0])
    if(i!=0):
        postorder(l1[1:i+1],l2[:i])
    if(i!=len(l1)-1):
        postorder(l1[i+1:],l2[i+1:])
    print(l1[0],end=" ")
t=int(input())
while(t):
    n=int(input())
    l1=list(map(int,input().split()))
    l2=[]
    l2=l2+l1
    l2.sort()
    postorder(l1,l2)
    print('\t')
    t=t-1
