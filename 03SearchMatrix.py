'''
编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：

每行的元素从左到右升序排列。
每列的元素从上到下升序排列。
示例:

现有矩阵 matrix 如下：

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
'''


def searchMatrix(matrix, target):
    """
    从矩阵的左下角开始比较

    目标值等于当前元素，返回 true；
    目标值大于当前元素，j 增 1，向右查找，排除掉此列上边的数据（都比当前元素更小）；
    目标值小于当前元素，i 减 1，向上查找，排除掉此行右边的数据（都比当前元素更大）。
    """
    if len(matrix) == 0:
        return False
    m, n = len(matrix), len(matrix[0])
    i, j = m - 1, 0
    while i >= 0 and j < n:
        if matrix[i][j] == target:
            return True
        if matrix[i][j] > target:
            i -= 1
        if matrix[i][j] < target:
            j += 1
    return False


if __name__ == '__main__':
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    print(searchMatrix(matrix, 5))
    print(searchMatrix(matrix, 100))
    print(searchMatrix(matrix, 20))
    pass
