# Input the data in rows (9 rows at time)
# convert the data in to list of lists or dict of dicts

row1 = input('Enter row1 of the Sudoko: ')
row2 = input('Enter row2 of the Sudoko: ')
row3 = input('Enter row3 of the Sudoko: ')
row4 = input('Enter row4 of the Sudoko: ')
row5 = input('Enter row5 of the Sudoko: ')
row6 = input('Enter row6 of the Sudoko: ')
row7 = input('Enter row7 of the Sudoko: ')
row8 = input('Enter row8 of the Sudoko: ')
row9 = input('Enter row9 of the Sudoko: ')


# convert to list of integers
def convert_to_list(row):
    result = [int(x) for x in row]
    return result


# check for duplicates and less 9 digits or more than 9 digits
def find_duplicate(res):
    find_duplicates = list(set(res))
    if len(find_duplicates) == 9:
        invalid_row = 'Yes'
    else:
        invalid_row = 'No'
    return invalid_row


def create_grid():
    invalid_row = 'No'
    cell_one_2_nine = []
    row1_list = convert_to_list(row1)
    row1_list_check = find_duplicate(row1_list)

    row2_list = convert_to_list(row2)
    row2_list_check = find_duplicate(row2_list)

    row3_list = convert_to_list(row3)
    row3_list_check = find_duplicate(row3_list)

    row4_list = convert_to_list(row4)
    row4_list_check = find_duplicate(row4_list)

    row5_list = convert_to_list(row5)
    row5_list_check = find_duplicate(row5_list)

    row6_list = convert_to_list(row6)
    row6_list_check = find_duplicate(row6_list)

    row7_list = convert_to_list(row7)
    row7_list_check = find_duplicate(row7_list)

    row8_list = convert_to_list(row8)
    row8_list_check = find_duplicate(row8_list)

    row9_list = convert_to_list(row9)
    row9_list_check = find_duplicate(row9_list)

    cell_one_2_nine = []
    if (
            row1_list_check == 'Yes' and row2_list_check == 'Yes' and
            row3_list_check == 'Yes' and row4_list_check == 'Yes' and
            row5_list_check == 'Yes' and row6_list_check == 'Yes' and
            row7_list_check == 'Yes' and row8_list_check == 'Yes' and
            row9_list_check == 'Yes'
    ):
        cell_one_2_nine.append(row1_list)
        cell_one_2_nine.append(row2_list)
        cell_one_2_nine.append(row3_list)
        cell_one_2_nine.append(row4_list)
        cell_one_2_nine.append(row5_list)
        cell_one_2_nine.append(row6_list)
        cell_one_2_nine.append(row7_list)
        cell_one_2_nine.append(row8_list)
        cell_one_2_nine.append(row9_list)

    else:
        invalid_row = 'Yes'

    return cell_one_2_nine


# validate row
def isRowValid(row_num):
    return len(set(sudoku[row_num])) == 9


# validate column
def isColValid(col_num):
    col = [item[col_num] for item in sudoku]
    return len(set(col)) == 9


# validate cell
def isCelValid(cel_row, cel_col):
    vals = sudoku[cel_row][cel_col: cel_col + 3]
    vals.extend(sudoku[cel_row + 1][cel_col: cel_col + 3])
    vals.extend(sudoku[cel_row + 2][cel_col: cel_col + 3])
    return len(set(vals)) == 9


# validate sudoku
def validateSudoku():
    for i in range(0, 9):
        if not isRowValid(i):
            return False
        if not isColValid(i):
            return False
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not isCelValid(i, j):
                return False
    return True

sudoku = create_grid()

if validateSudoku():
    print("Yes")
else:
    print("No")