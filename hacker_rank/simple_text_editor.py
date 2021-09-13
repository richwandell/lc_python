class TextEditor:

    def __init__(self):
        self.text = ""
        self.history = []

    def append(self, w):
        self.history.append(self.text)
        self.text += w

    def delete(self, k):
        self.history.append(self.text)
        self.text = self.text[0:-k]

    def print(self, k):
        if len(self.text) > k - 1:
            print(self.text[k-1])

    def undo(self):
        if len(self.history) > 0:
            self.text = self.history.pop()

if __name__ == "__main__":
    te = TextEditor()

    commands = [
        '1 abcde',
        '1 fg',
        '3 6',
        '2 5',
        '4',
        '3 7',
        '4',
        '3 4'
    ]
    num_operations = len(commands)
    # num_operations = int(input())
    for i in range(num_operations):
        # din = input()
        din = commands[i]

        if din[0] == '1':
            data = din.split(" ")
            te.append(data[1])
        elif din[0] == '2':
            data = din.split(" ")
            te.delete(int(data[1]))
        elif din[0] == '3':
            data = din.split(" ")
            te.print(int(data[1]))
        elif din[0] == '4':
            te.undo()
