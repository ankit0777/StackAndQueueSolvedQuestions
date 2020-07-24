# Given an integer K and a queue of integers, we need to reverse the order of the first K elements of the queue, leaving the other elements in the same relative order.
#
# Only following standard operations are allowed on queue.
#
# enqueue(x) : Add an item x to rear of queue
# dequeue() : Remove an item from front of queue
# size() : Returns number of elements in queue.
# front() : Finds front item.
def reverseK(queue,k,n):
    # code here
    lis=reversed(queue[0:k])
    lis2=queue[k:n]
    joinedList = [*lis, *lis2]
    return joinedList
