def insertion_sort(n_list, n):
    for i in range(n):
        focus_idx = i
        while focus_idx >= 1 and n_list[focus_idx-1] > n_list[focus_idx]:
            n_list[focus_idx], n_list[focus_idx-1] = n_list[focus_idx-1], n_list[focus_idx]
            focus_idx -= 1
        
        # print(n_list)
    return n_list

def selection_sort(n_list, n):
    for i in range(n):
        min_idx = i
        for j in range(i, n):
            if n_list[min_idx] > n_list[j]:
                min_idx = j

        n_list[i], n_list[min_idx] = n_list[min_idx], n_list[i]
        
        # print(n_list)
    return n_list

def bubble_sort(n_list, n):
    for i in range(n):
        # swap_check_flag = False
        for j in range(n-1-i):
            if n_list[j] > n_list[j+1]:
                # swap_check_flag = True
                n_list[j], n_list[j+1] = n_list[j+1], n_list[j] 
        
        # if not swap_check_flag:
        #     break
        
        # print(n_list)
    return n_list

n = int(input())
n_list = []

for _ in range(n):
    num = int(input())
    n_list.append(num)

insertion_sorted_list = insertion_sort(n_list[:], n)
print("\n".join(map(str, insertion_sorted_list)))

selection_sorted_list = selection_sort(n_list[:], n)
print("\n".join(map(str, selection_sorted_list)))

bubble_sorted_list = bubble_sort(n_list[:], n)
print("\n".join(map(str, bubble_sorted_list)))
