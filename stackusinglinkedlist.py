class Node:

    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    def push(self,ndata):
        new_node=Node(ndata)
        new_node.next = self.head
        self.head=new_node
    def pop(self):
        return self.head.data
        temp=self.head
        head=head.next
        temp.next=None
        free(temp)
    def traverse(self,d):
        temp=self.head
        c=0
        while(temp):
            if(temp.data==d):
                c=c+1
                return c
                break
            else:
                c=c+1
            temp=temp.next
        return -1

t=int(input())
if(1<=t<=50):
    for _ in range(t) :
        q=input()
        q=int(q)
        list1=list(input().split())

        llist=LinkedList()
        for s in range(len(list1)):
            if(list1[s]=='i'):
                llist.push(list1[s+1])
            elif(list1[s]=='r'):
                x=llist.pop()
                if(x==-1):
                    print("not present")
                else:
                    print(x)
                    print("present")
            elif(list1[s]=='f'):
                c=llist.traverse(list1[s+1])
                print(c)
