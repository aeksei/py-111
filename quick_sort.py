def quick_sort(arr: list[int]) -> list[int]:
    """"""
    if len(arr) <= 1:
        return arr

    pivot_value = arr[len(arr) // 2]  # опорный элемент
    return (
        quick_sort([value for value in arr if value < pivot_value]) +
        [value for value in arr if value == pivot_value] +
        quick_sort([value for value in arr if value > pivot_value])
    )


if __name__ == '__main__':
    assert quick_sort([]) == []
    assert quick_sort([1]) == [1]
    assert quick_sort([2, 1]) == [1, 2]
    assert quick_sort([3, 2, 1]) == [1, 2, 3]
    assert quick_sort([1, 2, 3]) == [1, 2, 3]

    assert quick_sort([4, 3, 3, 1, 2]) == [1, 2, 3, 4]

    src_list = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    result = quick_sort(src_list)

    print(src_list)
    print(result)
