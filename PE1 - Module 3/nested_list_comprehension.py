chessboard = [[str(column) + str(row) for column in 'ABCDEFGH'] for row in range(8, 0, -1)]
print(chessboard)
print()

print(chessboard[2])
print()

print(chessboard[2][6])
print()

chessboard[0][0] = 'ROOK'
chessboard[0][7] = 'ROOK'
chessboard[7][0] = 'ROOK'
chessboard[7][7] = 'ROOK'
print(chessboard)
print()

# To add a knight to c4
chessboard[4][2] = 'KNIGHT'
print(chessboard)
print()

# To add a pawn to E5
chessboard[3][4] = 'PAWN'
print(chessboard)
print()
