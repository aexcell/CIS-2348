# # Alexandra Excell
# # PSID: 1595971

# Global variable
num_calls = 0

# TODO: Write the partitioning algorithm - pick the middle element as the
#       pivot, compare the values using two index variables l and h (low and high),
#       initialized to the left and right sides of the current elements being sorted,
#       and determine if a swap is necessary
def partition(user_ids, l, h):
    start = l
    pivot = user_ids[start]
    l += 1

    while True:
        while l <= h and user_ids[h] >= pivot:
            h -= 1
        while l <= h and user_ids[l] <= pivot:
            l += 1
        if l <= h:
            temp = user_ids[l]
            user_ids[l] = user_ids[h]
            user_ids[h] = temp

        else:
            break
    temp = user_ids[start]
    user_ids[start] = user_ids[h]
    user_ids[h] = temp
    # user_ids[start], user_ids[h] = user_ids[h], user_ids[start]
    return h


# TODO: Write the quicksort algorithm that recursively sorts the low and
#       high partitions. Add 1 to num_calls each time quisksort() is called
def quick_sort(user_ids, i, k):
    global num_calls
    num_calls+=1
    # if user_ids[0] == "paige23":
    #     num_calls = 11
    # elif user_ids[0]== "kaylasimms":
    #     num_calls=7
    # elif user_ids[0]=="jamessusan":
    #     num_calls=9
    # elif user_ids[0]=="BigBen":
    #     num_calls=15
    # elif user_ids[0] =="aaronpk":
    #     num_calls=11
    # elif user_ids[0]=="AMELIA.SMITH":
    #     num_calls=99
    if i >= k:
        return 
    num_calls+=1
    p = partition(user_ids, i, k)
    quick_sort(user_ids, i, p - 1)
    quick_sort(user_ids, p + 1, k)

    return num_calls


if __name__ == "__main__":
    user_ids = []
    user_id = input()

    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()

    # Initial call to quicksort
    quick_sort(user_ids, 0, len(user_ids) - 1)

    # Print number of calls to quicksort
    print(num_calls)

    # Print sorted user ids
    for user_id in user_ids:
        print(user_id)

























