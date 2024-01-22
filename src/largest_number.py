
class LargestNumber:

    def find_largest_number(self, numbers: []) -> int:
        return self.find_largest_number_recursively(numbers, 0, len(numbers) - 1)

    def find_largest_number_recursively(self, numbers: [], start, end) -> int:
        if (end - start) == 1:
            if numbers[start] > numbers[end]:
                return numbers[start]
            else:
                return numbers[end]
        pivot = start + (end - start) // 2
        left_neighbour_idx = pivot - 1
        right_neighbour_idx = pivot + 1
        if (numbers[pivot] > numbers[left_neighbour_idx]) & (numbers[pivot] > numbers[right_neighbour_idx]):
            return numbers[pivot]
        if numbers[left_neighbour_idx] > numbers[pivot]:
            return self.find_largest_number_recursively(numbers, start, pivot)
        else:
            return self.find_largest_number_recursively(numbers, pivot + 1, end)
