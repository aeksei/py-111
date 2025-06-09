def factorial(n: int) -> int:
    """
    Сложность O(N)

    𝑛! = 1 * 2  * 3 * 4  * ...  * (𝑛−1)  * 𝑛
    :param n:
    :return:
    """
    if n == 0:
        return 1

    result = factorial(n - 1) * n
    return result


if __name__ == '__main__':
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
    assert factorial(5) == 120

    assert factorial(998)
