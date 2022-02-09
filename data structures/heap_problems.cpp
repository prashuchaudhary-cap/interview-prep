struct Node
{
    // val stores the element,
    // i stores list number of the element,
    // index stores column number of ith list from which element was taken
    int val, i, index;
};

// Comparison object to be used to order the min-heap
struct comp
{
    bool operator()(const Node &lhs, const Node &rhs) const
    {
        return lhs.val > rhs.val;
    }
};

// Function to merge M sorted lists each of size N and
// print them in ascending order
void printSorted(int list[][N])
{
    // create an empty min-heap
    priority_queue<Node, std::vector<Node>, comp> pq;

    // push first element of each list into the min-heap
    // along with list number and their index in the list
    for (int i = 0; i < M; i++)
        pq.push({list[i][0], i, 0});

    // run till min-heap is empty
    while (!pq.empty())
    {
        // extract minimum node from the min-heap
        Node min = pq.top();
        pq.pop();

        // print the minimum element
        cout << min.val << " ";

        // take next element from "same" list and
        // insert it into the min-heap
        if (min.index + 1 < N)
        {
            min.index += 1;
            min.val = list[min.i][min.index];
            pq.push(min);
        }
    }
}
