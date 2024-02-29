class MergeSort:
    @classmethod
    def _recursive_sort(cls, arr: list):
        if len(arr) < 2:
            return arr

        middle_pointer = len(arr) // 2
        left = cls._recursive_sort(arr[:middle_pointer])
        right = cls._recursive_sort(arr[middle_pointer:])
        return cls._merge_arrays(left, right)

    @classmethod
    def _merge_arrays(cls, left_part, right_part):
        result = []
        left_pointer = right_pointer = 0

        while left_pointer < len(left_part) and right_pointer < len(right_part):
            if left_part[left_pointer] < right_part[right_pointer]:
                result.append(left_part[left_pointer])
                left_pointer += 1
            else:
                result.append(right_part[right_pointer])
                right_pointer += 1

        if left_pointer < len(left_part):
            result.extend(left_part[left_pointer:])
        if right_pointer < len(right_part):
            result.extend(right_part[right_pointer:])
        return result

    @classmethod
    def execute(cls, arr: list) -> list:
        return cls._recursive_sort(arr)


if __name__=='__main__':

    # Проверяем работоспособность класса
    assert MergeSort.execute([1, 20, 3, 0, 0, 0, 0, 1]) == [0, 0, 0, 0, 1, 1, 3, 20]
    assert MergeSort.execute([]) == []
    assert MergeSort.execute([1]) == [1]
    assert MergeSort.execute([2, 1]) == [1, 2]
    assert MergeSort.execute([5, 5, 5, 0, 0, 0]) == [0, 0, 0, 5, 5, 5]
    assert MergeSort.execute([1, 0, -1, 57, -100, 100, 0, 0, 0]) == [-100, -1, 0, 0, 0, 0, 1, 57, 100]
