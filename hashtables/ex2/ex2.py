#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        currStr = ""
        curr = self.head
        while curr != None:
            currStr = f'{str(curr.value)} ->' + currStr
            curr = curr.next
        return currStr

    def insert_at_head(self, node):
        node.next = self.head
        self.head = node

def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here

    # initial a hash table
    buckets = {}

    for i in range(length):
        buckets[tickets[i].source] = tickets[i].destination

    linked_list = LinkedList()

    # insert the head
    linked_list.insert_at_head(Node(buckets["NONE"]))

    curr_node = linked_list.head

    # add to the head
    while curr_node.value != "NONE":
        linked_list.insert_at_head(Node(buckets[curr_node.value]))
        curr_node = linked_list.head

    currList = [None] * length

    i = length - 1
    curr = linked_list.head
    while curr != None:
        currList[i] = curr.value
        curr = curr.next
        i = i - 1

    return currList
