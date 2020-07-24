# import sys
# input = sys.stdin.readline

def process_queue(queue_list, f_idx, r_idx, command):
    cmd = command[0]
    if cmd == "push":
        queue_list[r_idx] = command[1]
        r_idx += 1
    elif cmd == "pop":
        if f_idx == r_idx:
            print(-1)
        else:
            print(queue_list[f_idx])
            f_idx += 1
    elif cmd == "size":
        print(r_idx-f_idx)
    elif cmd == "empty":
        print(int(r_idx == f_idx))
    elif cmd == "front":
        if f_idx == r_idx:
            print(-1)
        else:
            print(queue_list[f_idx])
    elif cmd == "back":
        if f_idx == r_idx:
            print(-1)
        else:
            print(queue_list[r_idx-1])

    return [f_idx, r_idx]
 
n = int(input())
queue_list = [0 for _ in range(n)]
f_idx = 0
r_idx = 0

for _ in range(n):
    command = input().split()
    f_idx, r_idx = process_queue(queue_list, f_idx, r_idx, command)