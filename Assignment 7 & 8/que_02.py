# Write a Python program to create a class representing a queue data structure. Include methods
# for enqueueing and dequeuing elements.

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return "Queue is empty"

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        print(" -> ".join(map(str, self.queue)))

if __name__ == "__main__":
    q = Queue()
    while True:
        print("\nOptions:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Display Queue")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            item = int(input("Enter value to enqueue: "))
            q.enqueue(item)
        elif choice == 2:
            print("Dequeued:", q.dequeue())
        elif choice == 3:
            q.display()
        elif choice == 4:
            break
        else:
            print("Invalid choice! Please try again.")