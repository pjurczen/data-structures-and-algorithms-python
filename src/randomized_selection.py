from quick_sort import QuickSort


class RandomizedSelection(QuickSort):
    def select(self, numbers: [], order_statistic: int) -> int:
        return self.select_recursive(numbers, 0, len(numbers), order_statistic)

    def select_recursive(self, numbers: [], start: int, end: [], order_statistic: int) -> int:
        if (end - start) <= 1:
            return numbers[start]
        pivot = self.select_pivot(numbers, start, end)
        partition = self.partition(numbers, pivot, start, end)
        if order_statistic == partition:
            return numbers[pivot]
        if partition > order_statistic:
            return self.select_recursive(numbers, start, partition, order_statistic)
        return self.select_recursive(numbers, partition + 1, end, order_statistic)
