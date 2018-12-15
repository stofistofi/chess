from chessboard import Chessboard

def test_create_board():
    # test whether creating a board is as expected
    expected_board =   { 0:'R',  1:'N',  2:'B',  3:'Q',  4:'K',  5:'B',  6:'N',  7:'R', 
                         8:'P',  9:'P', 10:'P', 11:'P', 12:'P', 13:'P', 14:'P', 15:'P',
                        16:' ', 17:' ', 18:' ', 19:' ', 20:' ', 21:' ', 22:' ', 23:' ',
                        24:' ', 25:' ', 26:' ', 27:' ', 28:' ', 29:' ', 30:' ', 31:' ',
                        32:' ', 33:' ', 34:' ', 35:' ', 36:' ', 37:' ', 38:' ', 39:' ',
                        40:' ', 41:' ', 42:' ', 43:' ', 44:' ', 45:' ', 46:' ', 47:' ',
                        48:'p', 49:'p', 50:'p', 51:'p', 52:'p', 53:'p', 54:'p', 55:'p',
                        56:'r', 57:'n', 58:'b', 59:'q', 60:'k', 61:'b', 62:'n', 63:'r'}
    c = Chessboard()
    try:
        assert c.current_board() == expected_board
        return True
    except:
        return False

def test_current_board():
    # test whether making a few moves changes the board correctly
    # this also tests move_pieces, which doesn't validate but only adjusts strings
    expected_board = { 0:'R',  1:'N',  2:'B',  3:'Q',  4:'K',  5:'B',  6:'N',  7:'R', 
                         8:'P',  9:'P', 10:' ', 11:'P', 12:' ', 13:'P', 14:'P', 15:'P',
                        16:' ', 17:' ', 18:' ', 19:' ', 20:' ', 21:' ', 22:' ', 23:' ',
                        24:' ', 25:' ', 26:'P', 27:' ', 28:'P', 29:' ', 30:' ', 31:' ',
                        32:' ', 33:' ', 34:' ', 35:' ', 36:' ', 37:' ', 38:' ', 39:' ',
                        40:'p', 41:' ', 42:' ', 43:' ', 44:' ', 45:'n', 46:' ', 47:' ',
                        48:' ', 49:'p', 50:'p', 51:'p', 52:'p', 53:'p', 54:'p', 55:'p',
                        56:'r', 57:'n', 58:'b', 59:'q', 60:'k', 61:'b', 62:' ', 63:'r'}
    c = Chessboard()
    c.move_piece(48,40)     # p to A3
    c.move_piece(10,26)     # P to C5
    c.move_piece(62,45)     # n to F3
    c.move_piece(12,28)     # P to E5

    try:
        assert c.current_board() == expected_board
        return True
    except:
        return False

def test_reveal_piece():
    # test whether keys reveal correct pieces before and after a few moves
    c = Chessboard()
    if ((c.reveal_piece(0) == 'R') and (c.reveal_piece(1) == 'N') and (c.reveal_piece(5) == 'B') and 
        (c.reveal_piece(11) == 'P') and (c.reveal_piece(49) == 'p') and (c.reveal_piece(56) == 'r') and 
        (c.reveal_piece(59) == 'q') and (c.reveal_piece(62) == 'n') and (c.reveal_piece(60) == 'k')):
        return True
    else:
        return False
    c.move_piece(52,36)     # p to E4
    c.move_piece(1, 18)     # N to C6
    c.move_piece(59,31)     # q to H4
    c.move_piece(13,29)     # P to E5
    if ((c.reveal_piece(36) == 'p') and (c.reveal_piece(18) == 'N') and (c.reveal_piece(31) == 'q') and 
        (c.reveal_piece(29) == 'P')):
        return True
    else:
        return False

def test_valid_input():
    c = Chessboard()
    try:
        assert c.valid_input('D2') == True
        assert c.valid_input('e5') == True
        assert c.valid_input('Zs') == False
        assert c.valid_input('1D') == False
        assert c.valid_input('231') == False
        assert c.valid_input('Þ34') == False
        assert c.valid_input('3e') == False
        assert c.valid_input('-3') == False
        assert c.valid_input(' d2') == False
        assert c.valid_input('d2 ') == False
        assert c.valid_input('') == False
        return True
    except:
        return False

def test_same_team():
    c = Chessboard()
    lower_case = True
    try:
        assert c.same_team(lower_case, 56) == True
        assert c.same_team(lower_case, 4) == False
        assert c.same_team(not lower_case, 48) == False 
        assert c.same_team(lower_case, 1) == False
        assert c.same_team(not lower_case, 60) == False
        assert c.same_team(lower_case, 58) == True
        return True
    except:
        return False

def test_move_pieces():
    # as move_pieces() only adjusts strings, the test has been 
    # implemented in test_current_board()
    return test_current_board()

print("Testing create_board():  ", test_create_board())
print("Testing current_board(): ",test_current_board())
print("Testing reveal_piece():  ", test_reveal_piece())
print("Testing valid_input():   ", test_valid_input())
print("Testing same_team:       ", test_same_team())
print("Testing move_pieces():   ", test_move_pieces())
