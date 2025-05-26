"""
Stack und Queue
Implementiere eine Stack-Struktur und eine Queue-Struktur sowie einfache
Operationen (push, pop, enqueue, dequeue).
"""


class Stack:
    def __init__(self, lst = None):
        if lst is None:
            self.stack = []
        elif isinstance(lst, list):
            self.stack = lst
        else:
            raise ValueError("Fehler: Parameter ist keine Liste.")

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if len(self.stack) == 0:
            print("Stack ist leer.")
            return None
        else:
            return self.stack.pop()

    def __str__(self):
        return f"{self.stack}"


class Queue:
    def __init__(self, lst = None):
        if lst is None:
            self.queue = []
        elif isinstance(lst, list):
            self.queue = lst
        else:
            raise ValueError("Fehler: Parameter ist keine Liste.")

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue ist leer.")
        else:
            return self.queue.pop(0)

    def __str__(self):
        return f"{self.queue}"


def main():
    """
    Test von Stack und Queue.
    """
    stack = Stack([1,2,3,4])
    print(f"Stack:         {stack}")
    stack.push(5)
    print(f"push(5)     -> {stack}")
    stack.pop()
    print(f"stack.pop() -> {stack}")
    print("")
    queue = Queue([1, 2, 3, 4, 5])
    print(f"Queue:         {queue}")
    queue.enqueue(5)
    print(f"enqueue(5)  -> {queue}")
    queue.dequeue()
    print(f"dequeue()   ->    {queue}")


if __name__ == '__main__':
    main()