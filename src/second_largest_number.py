
class SecondLargestNumber:
    def find_second_largest_number(self, numbers: []) -> int:
        largest_number, history = self.find_largest_number(numbers)
        second_largest_number = float("-inf")
        for i in history:
            if i > second_largest_number:
                second_largest_number = i
        return second_largest_number

    def find_largest_number(self, numbers: []) -> (int, []):
        if len(numbers) == 1:
            return numbers[0], []
        half_n = int(len(numbers) / 2)
        left_half = numbers[0:half_n]
        right_half = numbers[half_n:]
        left_result, left_history = self.find_largest_number(left_half)
        right_result, right_history = self.find_largest_number(right_half)
        if left_result > right_result:
            return left_result, left_history + [right_result]
        else:
            return right_result, right_history + [left_result]
