def romanToInt(s: str) -> int:
    sum: int = 0
    previous_value: int = 0
    chars_to_values: dict[str, int] = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for i in reversed(s):
        value: int = chars_to_values[i]
        if value < previous_value:
            sum -= value
        else:
            sum += value
        previous_value = value
    return sum
