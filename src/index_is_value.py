
class IndexIsValue:
    def index_is_value(self, sorted_num: [], start: int, end: int) -> int:
        if (end - start) == 1:
            if start < sorted_num[start]:
                return -1
            elif start > sorted_num[start]:
                return 1
            else:
                return 0
        pivot = start + (end - start) // 2
        left_slice_result = self.index_is_value(sorted_num, start, pivot)
        if (left_slice_result == -1) | (left_slice_result == 0):
            return left_slice_result
        return self.index_is_value(sorted_num, pivot, end)
