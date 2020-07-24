# Given a priority queue (max heap) and Q queries to be performed on priority queue. The task is to perform operations based on queries.
# 1. p : query to push element (x, given with query) to priority_queue and print size.
# 2. pp : query to pop element from priority_queue and print size.
# 3. t : query to return top element of priority_queue, if empty -1 will be printed.
void push_pq(priority_queue<int, vector<int>, greater<int>> &pq, int x){

    // Your code here
    pq.push(x);
}

/* Function to implement pop operation in priority_queue
* pq : priority_queue
*/
void pp_pq(priority_queue<int, vector<int>, greater<int>> &pq){

    if(!pq.empty())
    /*Your code here*/
    pq.pop();
    else
    return;

}

/* Function to implement top operation in priority_queue
* pq : priority_queue
*/
int pq_top(priority_queue<int, vector<int>, greater<int>> &pq){

    if(!pq.empty())
    /*Your code here*/
    return pq.top();
    else
    return -1;

}
