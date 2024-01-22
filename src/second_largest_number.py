
class SecondLargestNumber:
    def find_second_largest_number(self, numbers: []) -> int:
        largest_number = self.find_largest_number(numbers)
        second_largest_number = float("-inf")
        for i in numbers:
            if (i < largest_number) & (i > second_largest_number):
                second_largest_number = i
        return second_largest_number

    def find_largest_number(self, numbers: []) -> int:
        if len(numbers) == 1:
            return numbers[0]
        half_n = int(len(numbers) / 2)
        left_half = numbers[0:half_n]
        right_half = numbers[half_n:]
        left_result = self.find_largest_number(left_half)
        right_result = self.find_largest_number(right_half)
        largest_number = max(left_result, right_result)
        return largest_number
