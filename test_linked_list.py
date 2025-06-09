import pytest

from linked_list import LinkedList


def test_getitem():
    """"""
    ll = LinkedList()
    ll.append("Hello")

    assert ll[0] == "Hello"


def test_index_error():
    """"""
    ll = LinkedList()

    with pytest.raises(IndexError):
        ll[0]


def test_empty_linked_list_as_false():
    """"""
    ll = LinkedList()
    assert bool(ll) is False


def test_not_empty_linked_list_as_false():
    """"""
    ll = LinkedList()
    ll.append("Hello")

    assert bool(ll) is True