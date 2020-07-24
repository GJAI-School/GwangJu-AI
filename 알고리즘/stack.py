# import sys
# input = sys.stdin.readline

def process_stack(stack, size, command):
    cmd = command[0]
    if cmd == "push":
        stack.append(command[1])
        size += 1
    elif cmd == "pop":
        # try:
        #     print(stack.pop())
        #     size -= 1
        # except IndexError:
        #     print(-1)
        if size > 0:
            print(stack.pop())
            size -= 1
        else:
            print(-1)
    elif cmd == "size":
        print(size)
    elif cmd == "empty":
        if size == 0:
            print(1)
        else:
            print(0)
    elif cmd == "top":
        # try:
        #     print(stack[size-1])
        # except IndexError:
        #     print(-1)
        if size > 0:
            print(stack[size-1])
        else:
            print(-1)

    return [stack, size]
 
n = int(input())
stack = []
size = 0

for _ in range(n):
    command = input().split()
    stack, size = process_stack(stack, size, command)