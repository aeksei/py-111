def swap(arr: list[int], i: int, j: int) -> bool:
    is_swap = False
    left_item, right_item = arr[i], arr[j]
    if left_item > right_item:
        arr[i], arr[j] = right_item, left_item
        is_swap = True

    return is_swap


def bubble_sort(arr: list[int]) -> list[int]:
    """"""
    for j in range(len(arr)):
        last_index = len(arr) - 1 - j
        is_swapped = False

        for i in range(last_index):
            is_current_swap = swap(arr, i, i+1)
            if is_current_swap:
                is_swapped = True

        if not is_swapped:
            break

    return arr


if __name__ == '__main__':
    assert bubble_sort([]) == []
    assert bubble_sort([1]) == [1]
    assert bubble_sort([2, 1]) == [1, 2]
    assert bubble_sort([3, 2, 1]) == [1, 2, 3]
    assert bubble_sort([1, 2, 3]) == [1, 2, 3]

    assert bubble_sort([4, 3, 1, 2]) == [1, 2, 3, 4]
