"""
prepare game
"""

def  validate_board(board: list) -> bool:
    """
    this function determines whether the puzzle board is ready for play
    >>> validate_board(["**** ****","***1 ****","**  3****","* 4 1****",\
"     9 5 "," 6  83  *","3   1  **","  8  2***","  2  ****"])
    False
    """
    for i, line in enumerate(board):
        row_chek = []
        col_chek = []
        for j, el_row in enumerate(line):
            try:
                el_row = int(el_row)
                if el_row in row_chek:
                    return False
                row_chek.append(el_row)
            except ValueError:
                el_col = 0
            try:
                el_col = int(board[j][i])
                if el_col in col_chek:
                    return False
                col_chek.append(el_col)
            except ValueError:
                continue

    for i in range(5):
        color_chek = []
        for j in range(5):
            try:
                el_color = int(board[i + j][4 - i])
                if el_color in color_chek:
                    return False
                color_chek.append(el_color)
            except ValueError:
                if j == 4:
                    break
            try:
                el_color = int(board[4 + i][5 - i + j])
                if el_color in color_chek:
                    return False
                color_chek.append(el_color)
            except ValueError:
                continue

    return True
if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
