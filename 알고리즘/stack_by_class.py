# import sys
# input = sys.stdin.readline

class Stack:
    def __init__(self):
        self.array_list = []
        self.cnt = 0
    
    def push(self, value):
        self.array_list.append(value)
        self.cnt += 1
    
    def pop(self):
        if self.cnt > 0:
            self.cnt -= 1
            return self.array_list.pop()
        
        return -1
    
    def size(self):
        return self.cnt
    
    def empty(self):
        return int(self.cnt <= 0)
    
    def top(self):
        if self.cnt > 0:
            return self.array_list[self.cnt-1]        
        return -1

def process_stack(stack_list, command):
    cmd = command[0]
    if cmd == "push":
        stack_list.push(command[1])
    elif cmd == "pop":
        print(stack_list.pop())
    elif cmd == "size":
        print(stack_list.size())
    elif cmd == "empty":
        print(stack_list.empty())
    elif cmd == "top":
        print(stack_list.top())
 
n = int(input())
stack_list = Stack()

for _ in range(n):
    command = input().split()
    process_stack(stack_list, command)