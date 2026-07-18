class LinearQueue:

    def __init__(self, size=5):
        self.front = -1
        self.rear = -1
        self.size = size
        self.queue = [0] * size

    def overflow(self):
        return self.rear == self.size - 1

    def underflow(self):
        return self.front == -1 or self.front > self.rear

    def display(self):
        print(self.queue)

    def nq(self, data):
        if self.overflow():
            print("Overflow")

        elif self.front == -1:
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data

        else:
            self.rear += 1
            self.queue[self.rear] = data

    def dq(self):
        if self.underflow():
            print("Underflow")

        else:
            print(f"{self.queue[self.front]} item dequeued")
            self.queue[self.front] = 0
            self.front += 1


queue = LinearQueue()

choice = 1

while choice != 0:

    choice = int(input("Enter choice: "))

    match choice:

        case 1:
            data = int(input("Data? : "))
            queue.nq(data)

        case 2:
            queue.display()

        case 3:
            queue.dq()

        case 0:
            print("Program Ended")

        case _:
            print("Invalid Choice")