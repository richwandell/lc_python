class Queue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, num):
        self.stack1.append(num)

    def dequeue(self):
        if len(self.stack2) == 0 and len(self.stack1) > 0:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def print_front(self):
        if len(self.stack2) > 0:
            print(self.stack2[-1])
        else:
            print(self.stack1[0])



if __name__ == "__main__":


    q = Queue()
    # commands = [
    #     '1 42',
    #     '2',
    #     '1 14',
    #     '3',
    #     '1 28',
    #     '3',
    #     '1 60',
    #     '1 78',
    #     '2',
    #     '2'
    # ]

    commands = [
        '1 1',
        '1 2',
        '2',
        '3',
        '1 1',
        '3'
    ]

    for data in commands:
        if data[0] == '1':
            data = data.split(" ")
            q.enqueue(int(data[1]))
        elif data[0] == '2':
            q.dequeue()
        else:
            q.print_front()
