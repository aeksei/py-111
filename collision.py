"""
Без метода __eq__ но с одинаковыми хешами
first_node = Node("abc")
second_node = Node("abc")
third_node = Node("abc")
hash_table = {first_node: "a", second_node: "b", third_node: "c"}
# {Node("abc", None): "a", Node("abc", None): "b", Node("abc", None): "c"}

С методом __eq__ и одинаковыми хешами
# {Node("abc", None): "c"}
"""
