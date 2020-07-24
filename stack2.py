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



t=int(input())
if(1<=t<=50):
    for _ in range(t) :
        q=input()
        q=int(q)
        list1=list(input().split())

        s1=LinkedList()
        s2=LinkedList()

        for s in range(len(list1)):
            if(list1[s]=='i'):
                s1.push(list1[s+1])
            elif(list1[s]=='r'):
                temp=s1.head
                while(temp):
                    x=s1.pop()
                    s2.push(x)
                y=s2.pop()
                print(y)
                temp2=s2.head
                while(temp2):
                    z=s2.pop()
                    s1.push(z)
