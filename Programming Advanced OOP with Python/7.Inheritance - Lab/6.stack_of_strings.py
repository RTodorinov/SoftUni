class Stack:
    def __init__(self):
        self.data = []

    def push(self, element: str):
        self.data.append(element)

    def pop(self):
        element = self.data.pop()
        return element

    def top(self):
        return self.data[-1]

    def is_empty(self):
        if len(self.data) <= 0:
            return True
        return False

    # def is_empty(self):
    #     return not any(self.data)

    def __str__(self):
        reversed_data = list(reversed(self.data))
        return f"[{', '.join(reversed_data)}]"


# stack = Stack()
# print(stack.is_empty())
# print(stack)
# stack.push("asd")
# stack.push("hello")
# print(stack.is_empty())
# print(stack)
# print(stack.pop())
# print(stack)
# print(stack.top())
# print(stack)
