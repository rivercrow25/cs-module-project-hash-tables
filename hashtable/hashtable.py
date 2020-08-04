class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.tail = head

    def add_to_tail(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        self.tail.next = node
        self.tail = node

    def remove_node(self, key):
        cur = self.head
        if self.head.key == key:
            self.head = self.head.next
        else:
            while cur.next is not None:
                if cur.next.key == key:
                    cur.next = cur.next.next
                    if cur.next is None:
                        self.tail = cur.next
                cur = cur.next

    def find_node(self, key):
        cur = self.head
        if self.head.key == key:
            return self.head.value
        else:
            while cur is not None:
                if cur.key == key:
                    return cur.value
                cur = cur.next

    def replace_node(self, key, node):
        cur = self.head
        if cur.key == key:
            node.next = cur.next
            self.head = node
            return
        while cur.next is not None:
            if cur.next.key == key:
                node.next = cur.next.next
                cur.next = node
                if node.next is None:
                    self.tail = node
                return
        self.add_to_tail(node)

    def get_count(self):
        count = 0
        cur = self.head
        while cur is not None:
            count += 1
            cur = cur.next
        return count


        # Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.lst = [None] * capacity

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        items = 0
        for ll in self.lst:
            items += ll.get_count()
        return items / self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        pass

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 3313

        for char in key:
            hash = ((hash << 5) + hash) + ord(char)

        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        node = HashTableEntry(key, value)
        if self.lst[self.hash_index(key)] is not None:
            self.lst[self.hash_index(key)].replace_node(key, node)
        else:
            self.lst[self.hash_index(key)] = LinkedList(node)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        if self.lst[self.hash_index(key)].head.next is None:
            self.lst[self.hash_index(key)] = None
        else:
            self.lst[self.hash_index(key)].remove_node(key)

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        if self.lst[self.hash_index(key)] is not None:
            return self.lst[self.hash_index(key)].find_node(key)
        return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        oldlst = self.lst
        newlst = [None] * new_capacity
        self.lst = newlst
        self.capacity = new_capacity
        for ll in oldlst:
            cur = ll.head
            while cur is not None:
                self.put(cur.key, cur.value)
                cur = cur.next


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    # ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")
    print("")
    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))
    print(ht.get_load_factor())
    # Test resizing
    # old_capacity = ht.get_num_slots()
    # ht.resize(ht.capacity * 2)
    # new_capacity = ht.get_num_slots()

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))

    print("")
