# Your code here

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def find(self, value):
        curr = self.head
        while curr != None:
            if curr.value == value:
                return curr
            curr = curr.next
        return None
    
    def delete(self, value):
        curr = self.head

        if curr.value == value:
            self.head = curr.next
            curr.next = None
            return curr

        prev = None

        while curr != None:
            if curr.value == value:
                prev.next = curr.next
                curr.next = None
                return curr
            else:
                prev = curr
                curr = curr.next

        return None

    def insert_at_head(self, node):
        node.next = self.head
        self.head = node
        
    def insert_at_head_or_overwrite(self, node):
        existingNode = self.find(node.value)
        if existingNode != None:
            existingNode.value = node.value
        else: 
            self.insert_at_head(node)


class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __eq__(self, other):
        if isinstance(other, HashTableEntry):
            return self.key == other.key
        return False

class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.buckets = [None] * capacity
        self.capacity = capacity
        self.num_elements = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.buckets)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.num_elements / self.get_num_slots()

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for x in key:
            hash = ((hash << 5) + hash) + ord(x)
        return hash & 0xFFFFFFFF

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        hash_index = self.hash_index(key)
        if self.buckets[hash_index] != None:
            linked_list = self.buckets[hash_index]
            did_add_new_node = linked_list.insert_at_head_or_overwrite(Node(HashTableEntry(key, value)))
            if did_add_new_node:
                self.num_elements += 1
        else:
            linked_list = LinkedList()
            linked_list.insert_at_head(Node(HashTableEntry(key, value)))
            self.buckets[hash_index] = linked_list
            self.num_elements += 1

        if self.get_load_factor() > 0.7:
            self.resize(self.get_num_slots() * 2)

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        hash_index = self.hash_index(key)
        if self.buckets[hash_index] != None:
            linked_list = self.buckets[hash_index]

            node = linked_list.find(HashTableEntry(key, None))
            if node != None:
                return node.value.value
        return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here

        old_buckets = self.buckets
        self.buckets = [None] * int(new_capacity)
        self.num_elements = 0

        for element in old_buckets:
            if element == None:
                continue
            curr_node = element.head
            while curr_node != None:
                temp = curr_node.next
                curr_node.next = None
                hash_index = self.hash_index(curr_node.value.key)

                if self.buckets[hash_index] != None:
                    self.buckets[hash_index].insert_at_head(curr_node)
                else:
                    linked_list = LinkedList()
                    linked_list.insert_at_head(curr_node)
                    self.buckets[hash_index] = linked_list
                
                curr_node = temp
                self.num_elements += 1

def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here

    ht = HashTable(len(files))

    for value in files:
        strs = value.split("/")
        key = strs[len(strs) - 1]
        ht.put(key, value)

    result = []

    for q in queries:
        found = ht.get(q)
        if found:
            result.append(found)

    return result

# if __name__ == "__main__":
    # files = [
    #     '/bin/foo',
    #     '/bin/bar',
    #     '/usr/bin/baz'
    # ]
    # queries = [
    #     "foo",
    #     "qux",
    #     "baz"
    # ]
    # print(finder(files, queries))

files = []

for i in range(500000):
    files.append(f"/dir{i}/file{i}")

for i in range(500000):
    files.append(f"/dir{i}/dirb{i}/file{i}")

queries = []

for i in range(1000000):
    queries.append(f"nofile{i}")

queries += [
    "file3490",
    "file256",
    "file999999",
    "file8192"
]

print(finder(files, queries))