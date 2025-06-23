from functools import cache


@cache
def get_total_price(n: int, stairway_coasts: tuple[int, ...]) -> int:
    """

    :param n: Номер ступени до которой надо рассчитать стоимость
    :param stairway_coasts: Стоимость каждой ступени
    :return:
    """
    if n == 1:
        return stairway_coasts[0]
    if n == 2:
        return stairway_coasts[1]

    stair_index = n - 1
    stairway_coast = stairway_coasts[stair_index]  # Стоимость текущей ступени
    return stairway_coast + min(
        get_total_price(n-1, stairway_coasts),
        get_total_price(n-2, stairway_coasts),
    )


if __name__ == '__main__':
    assert get_total_price(4, (1, 3, 1, 5)) == 7