# Prabhu Roka
# 1986444
def selection_sort_descend_trace(int_list):
    list_size = len(int_list)
    for i in range(list_size - 1):
        max_index = i
        for j in range(i + 1, list_size):
            if int_list[j] > int_list[max_index]:
                max_index = j
        int_list[i], int_list[max_index] = int_list[max_index], int_list[i]
        print(" ".join(str(num) for num in int_list), end=' \n')


if __name__ == "__main__":
    input_list = [int(num) for num in input().split()]

    selection_sort_descend_trace(input_list)
