# Write a Python program to create a class representing a linked list data structure. Include
# methods for displaying linked list data, inserting and deleting nodes.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_node(self, key):
        temp = self.head

        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if not temp:
            print("Node with value", key, "not found.")
            return

        prev.next = temp.next
        temp = None

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Example usage
if __name__ == "__main__":
    ll = LinkedList()
    while True:
        print("\nOptions:")
        print("1. Insert at end")
        print("2. Insert at beginning")
        print("3. Delete a node")
        print("4. Display list")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            data = int(input("Enter value to insert at end: "))
            ll.insert_at_end(data)
        elif choice == 2:
            data = int(input("Enter value to insert at beginning: "))
            ll.insert_at_beginning(data)
        elif choice == 3:
            key = int(input("Enter value to delete: "))
            ll.delete_node(key)
        elif choice == 4:
            ll.display()
        elif choice == 5:
            break
        else:
            print("Invalid choice! Please try again.")