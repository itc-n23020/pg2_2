def is_valid_chess_board(board):
    piece_count = {
        'wking': 0, 'bking': 0,
        'wpawn': 0, 'bpawn': 0,
        'wqueen': 0, 'bqueen': 0,
        'wrook': 0, 'brook': 0,
        'wbishop': 0, 'bbishop': 0,
        'wknight': 0, 'bknight': 0,
    }
    
    def is_valid_position(position):
        if len(position) != 2:
            return False
        row, col = position
        return row in '12345678' and col in 'abcdefgh'

    def is_valid_piece(piece):
        return piece in piece_count

    for position, piece in board.items():
        if not is_valid_position(position):
            return False
        if not is_valid_piece(piece):
            return False
        piece_count[piece] += 1

    if piece_count['wking'] != 1 or piece_count['bking'] != 1:
        return False
    if piece_count['wpawn'] > 8 or piece_count['bpawn'] > 8:
        return False

    total_white_pieces = sum(count for piece, count in piece_count.items() if piece.startswith('w'))
    total_black_pieces = sum(count for piece, count in piece_count.items() if piece.startswith('b'))
    
    if total_white_pieces > 16 or total_black_pieces > 16:
        return False

    return True

board = {
    '1h': 'bking', '6c': 'wqueen', '2g': 'bbishop',
    '5h': 'bqueen', '3e': 'wking'
}

print(is_valid_chess_board(board))  
