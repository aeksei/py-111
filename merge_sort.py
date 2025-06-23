def merge_func(left_part: list[int], right_part: list[int]) -> list[int]:
    """"""


def merge_sort(arr: list[int]) -> list[int]:
    size_arr = len(arr)
    if size_arr <= 1:
        return arr

    middle_index = size_arr // 2
    left_part = arr[:middle_index]
    right_part = arr[middle_index:]

    left_part = merge_sort(left_part)
    right_part = merge_sort(right_part)

    return merge_func(left_part, right_part)
