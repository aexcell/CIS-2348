# Alexandra Excell
# PSID: 1595971

# WORKS
# def selection_sort_descend_trace(numbers):
#     numbers = [int(i) for i in numbers]
#     for idx,num in enumerate(numbers):
#         max_num = max(numbers[idx:])
#         max_idx = numbers.index(max_num)
#         if num < max_num:
#             numbers[idx] = max_num
#             numbers[max_idx] = num
#             print(*numbers,sep=' ', end=' \n')

def selection_sort_descend_trace(numbers):
    numbers = list(numbers.split(sep=' '))
    numbers = [int(i) for i in numbers]
    for idx,num in enumerate(numbers):
        max_num = max(numbers[idx:])
        max_idx = numbers.index(max_num)
        if num < max_num:
            numbers[idx] = max_num
            numbers[max_idx] = num
            print(*numbers,sep=' ', end=' \n')
        else:
            if idx < len(numbers)-1:
                print(*numbers, sep=' ', end=' \n')
    sorted_numbers = numbers
    return sorted_numbers


if __name__ == "__main__":
    # TODO: Read in a list of integers into numbers, then call
    #       selection_sort_descend_trace() to sort the numbers
    numbers = input()
    # numbers2 = '45 79 52 33 88'
    selection_sort_descend_trace(numbers)













