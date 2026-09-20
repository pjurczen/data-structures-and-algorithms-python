class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        previousRow = [1]
        for row in range(1, rowIndex + 1):
            previousLeft = 1
            for idx in range(1, row):
                leftNum = previousLeft
                rightNum = previousRow[idx]
                previousLeft = previousRow[idx]
                previousRow[idx] = leftNum + rightNum
            previousRow.append(1)
        return previousRow
