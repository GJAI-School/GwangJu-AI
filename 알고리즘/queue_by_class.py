# import sys
# input = sys.stdin.readline

class Queue:
    def __init__(self, length):
        self.array_list = [0 for _ in range(length)]
        self.f_idx = 0
        self.r_idx = 0
    
    def push(self, value):
        self.array_list[self.r_idx] = value
        self.r_idx += 1
    
    def pop(self):
        if self.f_idx == self.r_idx:
            return -1
        
        self.f_idx += 1
        return self.array_list[self.f_idx-1]
    
    def size(self):
        return (self.r_idx - self.f_idx)
    
    def empty(self):
        # return int(self.size() <= 0)
        if self.size() > 0:
            return 0
        
        return 1
    
    def front(self):
        if self.size() > 0:
            return self.array_list[self.f_idx]
        
        return -1

    def back(self):
        if self.size() > 0:
            return self.array_list[self.r_idx-1]
        
        return -1

def process_queue(queue_list, command):
    cmd = command[0]
    if cmd == "push":
        queue_list.push(command[1])
    elif cmd == "pop":
        print(queue_list.pop())
    elif cmd == "size":
        print(queue_list.size())
    elif cmd == "empty":
        print(queue_list.empty())
    elif cmd == "front":
        print(queue_list.front())
    elif cmd == "back":
        print(queue_list.back())
 
n = int(input())
queue_list = Queue(length=n)

for _ in range(n):
    command = input().split()
    process_queue(queue_list, command)