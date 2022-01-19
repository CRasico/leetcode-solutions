class MinStackNode:
    def __init__(self, x: int):
        self.value = x
        self.previous = None

class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_node = None

    def push(self, x: int) -> None:
        temp_node = MinStackNode(x)
        temp_node.previous = self.min_node
        if self.min_node == None:
            self.min_node = temp_node
        elif temp_node.value < self.min_node.value:
            self.min_node = temp_node
        self.stack.append(temp_node)

    def pop(self) -> None:
        if self.min_node != None:
            temp_node = self.stack.pop(len(self.stack) - 1)
            if temp_node == self.min_node:
                self.min_node = temp_node.previous
        

    def top(self) -> int:
        if self.min_node != None:
            return self.stack[len(self.stack) - 1].value
        return None

    def getMin(self) -> int:
        return self.min_node.value
