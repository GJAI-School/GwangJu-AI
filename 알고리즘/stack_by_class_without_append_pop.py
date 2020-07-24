# import sys
# input = sys.stdin.readline

class Stack:
    def __init__(self, n):
        self.array = [0 for _ in range(n)]
        self.length = 0
    
    def push(self, value):
        self.array[self.length] = value
        self.length += 1

    def pop(self):
        if self.length == 0:
            return -1
        
        self.length -= 1
        return self.array[self.length]
    
    def size(self):
        return self.length

    def empty(self):
        if self.length == 0:
            return 1
        
        return 0
        # return int(self.length == 0)

    def top(self):
        if self.length == 0:
            return -1
        
        return self.array[self.length-1]
        
def process_stack(stack_instance, command):
    if command[0] == "push":
        stack_instance.push(command[1])
    elif command[0] == "pop":
        print(stack_instance.pop())
    elif command[0] == "size":
        print(stack_instance.size())
    elif command[0] == "empty":
        print(stack_instance.empty())
    elif command[0] == "top":
        print(stack_instance.top())
    
n = int(input())
stack_instance = Stack(n)

for _ in range(n):
    command = input().split()
    process_stack(stack_instance, command)