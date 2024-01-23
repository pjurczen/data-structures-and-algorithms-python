
class QuickSort:
    def sort(self, numbers: []):
        self.sort_recursive(numbers, 0, len(numbers))

    def sort_recursive(self, numbers: [], start: int, end: int):
        if (end - start) <= 1:
            return
        pivot = self.select_pivot(numbers, start, end)
        partition = self.partition(numbers, pivot, start, end)
        self.sort_recursive(numbers, start, partition)
        self.sort_recursive(numbers, partition + 1, end)

    def partition(self, numbers: [], pivot: int, start: int, end: int) -> int:
        pivot_value = numbers[pivot]
        self.swap(numbers, pivot, start)
        i = start + 1
        for j in range(start + 1, end - start):
            if numbers[j] < pivot_value:
                self.swap(numbers, i, j)
                i += 1
        self.swap(numbers, start, i - 1)
        return i - 1

    def select_pivot(self, numbers: [], start: int, end: int) -> int:
        return end - 1

    def swap(self, numbers, x, y):
        tmp = numbers[x]
        numbers[x] = numbers[y]
        numbers[y] = tmp
