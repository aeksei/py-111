MIN_VALUE = 0
MAX_VALUE = 9

def counting_sort(arr):
    counting = [0] * (MAX_VALUE + 1)

    for value in arr:
        counting[value] += 1

    result = []
    for index, count in enumerate(counting):
        result.extend([index] * count)

    return result


if __name__ == '__main__':
    assert counting_sort([4, 4, 4, 4, 3, 3, 3, 2, 2, 1]) == [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]