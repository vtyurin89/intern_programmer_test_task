from typing import Any




class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class EpicCircularQueueTwo:

    # Циклический буфер на основе связного списка.
    def __init__(self, size: int):
        self.__check_size(size)
        self._max_size = size
        self._current_size = 0
        self._head_pointer = self._tail_pointer = creation_pointer = ListNode(value=None)
        for _ in range(size - 1):
            creation_pointer.next = ListNode(value=None)
            creation_pointer = creation_pointer.next
        creation_pointer.next = self._head_pointer

    def __check_size(self, value) -> None:
        if type(value) != int or value <= 0:
            raise ValueError("Укажите корректный размер кольцевого буфера!")

    def check_if_empty(self) -> bool:
        return self._current_size == 0

    def check_if_full(self) -> bool:
        return self._current_size == self._max_size

    def list_values(self) -> list:
        if self.check_if_empty() is True:
            return []
        values = []
        current_node = self._head_pointer
        for _ in range(self._current_size):
            values.append(current_node.value)
            current_node = current_node.next
        return values

    def add_value(self, value) -> None:
        if self.check_if_full() is True:
            print("Кольцевой буфер полон.")
            return
        self._tail_pointer.value = value
        self._tail_pointer = self._tail_pointer.next
        self._current_size += 1

    def headpop_value(self) -> Any:
        if self.check_if_empty() is True:
            print("Кольцевой буфер пуст.")
            return
        value = self._head_pointer.value
        self._head_pointer.value = None
        self._head_pointer = self._head_pointer.next
        self._current_size -= 1
        return value


if __name__ == "__main__":

    # Проверяем работоспособность класса
    circular_queue_2 = EpicCircularQueueTwo(size=10)
    assert circular_queue_2.check_if_empty() is True
    for i in range(10):
        circular_queue_2.add_value(i)
    assert circular_queue_2.list_values() == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert circular_queue_2.check_if_full() is True
    assert circular_queue_2.headpop_value() == 0
    assert circular_queue_2.headpop_value() == 1
    assert circular_queue_2.headpop_value() == 2
    assert circular_queue_2.check_if_full() is False
    circular_queue_2.add_value(10)
    circular_queue_2.add_value(11)
    circular_queue_2.add_value(12)
    circular_queue_2.headpop_value()
    circular_queue_2.add_value(13)
    assert circular_queue_2.list_values() == [4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    assert circular_queue_2.check_if_full() is True
    circular_queue_2.add_value(666)
    assert circular_queue_2.list_values() == [4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
