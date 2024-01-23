import numpy as np


class QuickSort:
    def sort(self, numbers: []):
        number_of_calls = self.sort_recursive(numbers, 0, len(numbers))
        print("Number of calls: " + str(number_of_calls))

    def sort_recursive(self, numbers: [], start: int, end: int) -> int:
        number_of_calls = end - start - 1
        if (end - start) <= 1:
            return 0
        pivot = self.select_pivot(numbers, start, end)
        partition = self.partition(numbers, pivot, start, end)
        ret_calls_left = self.sort_recursive(numbers, start, partition)
        ret_calls_right = self.sort_recursive(numbers, partition + 1, end)
        return number_of_calls + ret_calls_right + ret_calls_left

    def partition(self, numbers: [], pivot: int, start: int, end: int) -> int:
        pivot_value = numbers[pivot]
        self.swap(numbers, pivot, start)
        i = start + 1
        for j in range(start + 1, end):
            if numbers[j] < pivot_value:
                self.swap(numbers, i, j)
                i += 1
        self.swap(numbers, start, i - 1)
        return i - 1

    def select_pivot(self, numbers: [], start: int, end: int) -> int:
        middle = start + (end - 1 - start) // 2
        start_value = numbers[start]
        end_value = numbers[end - 1]
        middle_value = numbers[middle]
        values = [start_value, end_value, middle_value]
        median = int(np.median(values))
        if median == start_value:
            return start
        if median == end_value:
            return end - 1
        return middle

    def swap(self, numbers, x, y):
        tmp = numbers[x]
        numbers[x] = numbers[y]
        numbers[y] = tmp
