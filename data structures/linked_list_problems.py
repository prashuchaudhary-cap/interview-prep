
class Node:
    '''Structure of linked list node'''

    def __init__(self, data):
        self.data = data
        self.next = None
        self.random = None


def clone(original_root):
    '''Clone a doubly linked list with random pointer'''
    '''with O(1) extra space'''

    '''Insert additional node after every node of original list'''
    curr = original_root
    while curr != None:
        new = Node(curr.data)
        new.next = curr.next
        curr.next = new
        curr = curr.next.next

    '''Adjust the random pointers of the newly added nodes'''
    curr = original_root
    while curr != None:
        curr.next.random = curr.random.next
        curr = curr.next.next

    '''Detach original and duplicate list from each other'''
    curr = original_root
    dup_root = original_root.next
    while curr.next != None:
        tmp = curr.next
        curr.next = curr.next.next
        curr = tmp

    return dup_root



class Node:

    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to print it the linked LinkedList
    def print_list(self):
        temp = self.head
        while(temp):
            print temp.data,
            temp = temp.next

    def detect_loop(self):
        slow_p = self.head
        fast_p = self.head
        while(slow_p and fast_p and fast_p.next):
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p:
                return True

        return False

# Driver program for testing
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(10)

# Create a loop for testing
llist.head.next.next.next.next = llist.head
if(llist.detectLoop()):
        print "Found Loop"
else:
        print "No Loop"


#include <bits/stdc++.h>
using namespace std;

/* Link list node */
struct Node {
    int data;
    struct Node* next;
};

// Fucntion to delete the node without head
void deleteNodeWithoutHead(struct Node* pos)
{
    if (pos == NULL) // If linked list is empty
        return;
    else {
        if (pos->next == NULL) {
            printf("This is last node, require head, can't be freed\n");
            return;
        }

        struct Node* temp = pos->next;

        // Copy data of the next node to current node
        pos->data = pos->next->data;

        // Perform conventional deletion
        pos->next = pos->next->next;

        free(temp);
    }
}
