from typing import Any


class EpicCircularQueueOne:

    # Циклический буфер на основе списка
    def __init__(self, size: int):
        self.__check_size(size)
        self._max_size = size
        self.data = [None] * size
        self._head_pointer = self._tail_pointer = 0
        self._current_size = 0

    def __check_size(self, value) -> None:
        if type(value) != int or value <= 0:
            raise ValueError("Укажите корректный размер кольцевого буфера!")

    def check_if_empty(self) -> bool:
        return self._current_size == 0

    def check_if_full(self) -> bool:
        return self._current_size == self._max_size

    def list_values(self) -> list:
        return [item for item in self.data if item is not None]

    def add_value(self, value) -> None:
        if self.check_if_full() is True:
            print("Кольцевой буфер полон.")
            return
        self.data[self._tail_pointer] = value
        self._current_size += 1
        self._tail_pointer = (self._tail_pointer + 1) % self._max_size

    def headpop_value(self) -> Any:
        if self.check_if_empty() is True:
            print("Кольцевой буфер пуст.")
            return
        value = self.data[self._head_pointer]
        self.data[self._head_pointer] = None
        self._current_size -= 1
        self._head_pointer = (self._head_pointer + 1) % self._max_size
        return value


if __name__ == "__main__":

    # Проверяем работоспособность класса
    circular_queue_1 = EpicCircularQueueOne(size=10)
    assert circular_queue_1.check_if_empty() is True
    for i in range(10):
        circular_queue_1.add_value(i)
    assert circular_queue_1.check_if_full() is True
    assert circular_queue_1.headpop_value() == 0
    assert circular_queue_1.headpop_value() == 1
    assert circular_queue_1.headpop_value() == 2
    assert circular_queue_1.check_if_full() is False
    circular_queue_1.add_value(10)
    circular_queue_1.add_value(11)
    circular_queue_1.add_value(12)
    circular_queue_1.headpop_value()
    circular_queue_1.add_value(13)
    assert circular_queue_1.list_values() == [10, 11, 12, 13, 4, 5, 6, 7, 8, 9]
    assert circular_queue_1.check_if_full() is True
    circular_queue_1.add_value(666)
    assert circular_queue_1.list_values() == [10, 11, 12, 13, 4, 5, 6, 7, 8, 9]
