def heapify(nums, heap_size, root_index):
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        heapify(nums, heap_size, largest)


def heap_sort(nums):
    n = len(nums)

    for i in range(n, -1, -1):
        heapify(nums, n, i)

    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)


def is_anagram(first_string, second_string):
    if first_string == '' and second_string == '':
        return ('', '', False)

    first_list = [lt for lt in first_string.lower()]
    second_list = [lt for lt in second_string.lower()]

    heap_sort(first_list)
    heap_sort(second_list)

    fisrt_anagram = ''.join(first_list)
    second_anagram = ''.join(second_list)

    is_anagram = fisrt_anagram == second_anagram

    return (fisrt_anagram, second_anagram, is_anagram)
