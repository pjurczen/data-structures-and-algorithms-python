# Time complexity: O(n^2)
# Space complexity: O(n^2)

def generate(numRows: int) -> list[list[int]]:
    prevRow: list[int] = [1]
    output: list[list[int]] = [prevRow]
    for row in range(2, numRows + 1):
        currRow: list[int] = []
        lenPrevRow = len(prevRow)
        for i in range(0, row):
            leftNum = prevRow[i - 1] if i - 1 >= 0 else 0
            rightNum = prevRow[i] if i < lenPrevRow else 0
            currRow.append(leftNum + rightNum)
        prevRow = currRow
        output.append(currRow)
    return output
