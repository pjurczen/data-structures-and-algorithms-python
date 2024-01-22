import numpy as np
from numpy import NaN


class LocalMinimum:
    def find_local_minimum(self, numbers) -> int:
        rows_count = len(numbers)
        columns_count = len(numbers[0])
        pivot_row = rows_count // 2
        pivot_column = columns_count // 2
        return self.find_local_minimum_recursive(numbers, pivot_row, pivot_column)

    def find_local_minimum_recursive(self, numbers, pivot_row, pivot_column) -> int:
        max_row_index = len(numbers) - 1
        max_column_index = len(numbers[0]) - 1
        pivot = numbers[pivot_row][pivot_column]
        if pivot_row < max_row_index:
            value_down = numbers[pivot_row + 1][pivot_column]
        else:
            value_down = float("+inf")
        if pivot_row > 0:
            value_up = numbers[pivot_row - 1][pivot_column]
        else:
            value_up = float("+inf")
        if pivot_column < max_column_index:
            value_right = numbers[pivot_row][pivot_column + 1]
        else:
            value_right = float("+inf")
        if pivot_column > 0:
            value_left = numbers[pivot_row][pivot_column - 1]
        else:
            value_left = float("+inf")
        neighbours = [value_left, value_right, value_up, value_down]
        if min(neighbours) > pivot:
            return pivot
        lowest_neighbour = np.argmin(neighbours)
        if lowest_neighbour == 0:
            return self.find_local_minimum_recursive(numbers, pivot_row, pivot_column - 1)
        if lowest_neighbour == 1:
            return self.find_local_minimum_recursive(numbers, pivot_row, pivot_column + 1)
        if lowest_neighbour == 2:
            return self.find_local_minimum_recursive(numbers, pivot_row - 1, pivot_column)
        if lowest_neighbour == 3:
            return self.find_local_minimum_recursive(numbers, pivot_row + 1, pivot_column)
        return NaN
