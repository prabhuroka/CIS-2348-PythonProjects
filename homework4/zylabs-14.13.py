# Prabhu Roka
# 1986444
# Global variable
num_calls = 0


# TODO: Write the partitioning algorithm - pick the middle element as the
#       pivot, compare the values using two index variables l and h (low and high),
#       initialized to the left and right sides of the current elements being sorted,
#       and determine if a swap is necessary
def partition(user_id1, i, k):
    pivot = user_id1[(i + k) // 2]
    l = i
    h = k
    while True:
        while user_id1[l] < pivot:
            l += 1
        while user_id1[h] > pivot:
            h -= 1
        if l >= h:
            return h
        user_id1[l], user_id1[h] = user_id1[h], user_id1[l]
        l += 1
        h -= 1


# TODO: Write the quicksort algorithm that recursively sorts the low and
#       high partitions. Add 1 to num_calls each time quicksort() is called
def quicksort(user_id1, i, k):
    global num_calls
    num_calls += 1
    if i >= k:
        return
    j = partition(user_id1, i, k)
    quicksort(user_id1, i, j)
    quicksort(user_id1, j + 1, k)


if __name__ == "__main__":
    user_ids = []
    user_id = input()
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()

    # Initial call to quicksort
    quicksort(user_ids, 0, len(user_ids) - 1)

    # Print number of calls to quicksort
    print(num_calls)

    # Print sorted user ids
    for user_id in user_ids:
        print(user_id)
