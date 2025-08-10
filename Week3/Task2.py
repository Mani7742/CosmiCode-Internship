def reverse_list(lst):
    reversed_lst = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst

if __name__ == "__main__":
    original_list = [1, 2, 3, 4, 5, 6]
    print("Original list:", original_list)
    reversed_list = reverse_list(original_list)
    print("Reversed list:", reversed_list)