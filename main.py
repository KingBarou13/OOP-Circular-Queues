class Queue:
    def __init__(self, size):
        self.queueArray = [None] * size
        self.front = -1
        self.rear = -1
        self.max_size = size

    def isEmpty(self):
        return self.front - self.rear ==0

    def isFull(self):
        return (self.rear + 1) % self.max_size == self.front

    def enqueue(self, item):
        if self.isFull():
            print("Queue is full")
            return
        self.rear = (self.rear + 1) % self.max_size
        self.queueArray[self.rear] = item

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
            return None

        dequeued_item = self.queueArray[self.front]
        self.queueArray[self.front] = None

        self.front = (self.front + 1) % self.max_size

        return dequeued_item

    def size(self):
        if self.isEmpty():
            return 0
        if self.rear >= self.front:
            return self.rear - self.front + 1
        else:
            return self.max_size - self.front + self.rear + 1


size = int(input("Enter the size of the queue: "))
queue = Queue(size)

while True:
    print("\nChoose an option:")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Check Size")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        item = input("Enter the item to enqueue: ")
        queue.enqueue(item)
    elif choice == 2:
        dequeued_item = queue.dequeue()
        if dequeued_item is not None:
            print("Dequeued item: " + dequeued_item)
    elif choice == 3:
        print("Queue size: ", queue.size())
    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid choice, please try again.")
