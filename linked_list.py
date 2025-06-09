from typing import Any, Optional


class Node:
    """Узел связанного списка."""
    def __init__(
        self,
        value: Any,
        next_: Optional["Node"] = None,
    ):
        self.value = value
        self.next = next_


class LinkedList:
    def __init__(self):
        """"""
        self.head: Node | None = None
        self._len: int = 0

    def append(self, value: Any) -> None:
        """Добавить узел в конец списка."""
        append_node = Node(value)

        if not self.head:
            self.head = append_node
        else:
            last_index = self._len - 1
            tail = self._step_by_step(last_index)
            tail.next = append_node

        self._len += 1

    def _step_by_step(self, i: int) -> Node:
        """Дойти до нужно узла и вернуть его."""
        current_node = self.head
        for _ in range(i):
            current_node = current_node.next

        return current_node

    def __getitem__(self, i: int) -> Any:
        """
        Возвращать значение по указанному индексу.

        :param i:
        :return:

        >>> ll = LinkedList()
        >>> ll.append("Hello")
        >>> ll[0]  # __getitem__
        'Hello'
        """
        print("Вызов метода __getitem__")
        if i >= self._len:
            raise IndexError("Вываливаюсь за границы диапазона")

        current_node = self._step_by_step(i)
        return current_node.value

    def __len__(self) -> int:
        print("__len__")
        return self._len


if __name__ == '__main__':
    ll = LinkedList()
    ll.append("Hello")
    ll.append("World")

    # TODO Алгоритмическая сложность цикла
    for value in ll:
        print(value)

    # TODO Алгоритмическая сложность метода contains
    print("World" in ll)
    print("Does not exist item" in ll)

    # TODO Алгоритмическая сложность сортировки через sorted
    print(sorted(ll))  # O(N * log(N)))

    # TODO Алгоритмическая сложность сортировки через sorted
    for value in reversed(ll):  # for i in range(len(ll), -1, -1): ll[i]
        print(value)
