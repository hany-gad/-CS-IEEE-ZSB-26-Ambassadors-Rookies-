for i in range(1, 6):
    row = input().split()
    for j in range(1, 6):
        if row[j - 1] == '1':
            r = i
            c = j
row_moves = abs(r - 3)
col_moves = abs(c - 3)
total_moves = row_moves + col_moves
print(total_moves)