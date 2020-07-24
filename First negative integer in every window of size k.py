# Given an array and a positive integer k, find the first negative integer for each and every window(contiguous subarray) of size
#code
t=int(input())
while(t):
    n=int(input())
    l1=list(map(int,input().split()))
    k=int(input())
    flag2=0
    for i in range(0,n-k+1):
        flag=0
        for j in range(i,i+k):
            if(j==n):
                flag2=1
                break
            if(l1[j]<0):
                print(l1[j],end=" ")
                flag=1
                break
        if(flag2==1):
            break
        if(flag==0):
            print(0,end=" ")
    print()
    t=t-1
