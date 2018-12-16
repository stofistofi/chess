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

def test_horizontal_travel():
    # test horizontal travel of pieces, before data is sent to that function
    # another validates that the movement is in the horizontal line on the board
    c = Chessboard()
    c.move_piece(48,32)     # p to A4
    c.move_piece(15,31)     # P to H5
    c.move_piece(56,40)     # r to A3
    c.move_piece(7,23)      # R to H6
    c.move_piece(51,43)     # p to D3
    c.move_piece(11,19)     # P to D6
    '''{ 0:'R',  1:'N',  2:'B',  3:'Q',  4:'K',  5:'B',  6:'N',  7:' ', 
         8:'P',  9:'P', 10:'P', 11:' ', 12:'P', 13:'P', 14:'P', 15:' ',
        16:' ', 17:' ', 18:' ', 19:'P', 20:' ', 21:' ', 22:' ', 23:'R',
        24:' ', 25:' ', 26:' ', 27:' ', 28:' ', 29:' ', 30:' ', 31:'P',
        32:'p', 33:' ', 34:' ', 35:' ', 36:' ', 37:' ', 38:' ', 39:' ',
        40:'r', 41:' ', 42:' ', 43:'p', 44:' ', 45:' ', 46:' ', 47:' ',
        48:' ', 49:'p', 50:'p', 51:' ', 52:'p', 53:'p', 54:'p', 55:'p',
        56:' ', 57:'n', 58:'b', 59:'q', 60:'k', 61:'b', 62:'n', 63:'r'}'''
    try:
        assert c.horizontal_travel(40,41) == True
        assert c.horizontal_travel(40,42) == True
        # moving r from 40 to 43 on p would be OK with horizontal_travel because it
        # only checks whether we've jumped any pieces, other validating functions
        # make sure we can't kill our own pieces
        assert c.horizontal_travel(40,44) == False
        assert c.horizontal_travel(40,24) == False
        assert c.horizontal_travel(23,39) == False
        assert c.horizontal_travel(23,18) == False
        assert c.horizontal_travel(23,20) == True
        return True
    except:
        return False

def test_vertical_travel():
    c = Chessboard()
    c.move_piece(48,32)     # p to A4
    c.move_piece(15,31)     # P to H5
    c.move_piece(56,40)     # r to A3
    c.move_piece(7,23)      # R to H6
    c.move_piece(51,43)     # p to D3
    c.move_piece(11,19)     # P to D6
    c.move_piece(40,41)     # r to B3
    '''{ 0:'R',  1:'N',  2:'B',  3:'Q',  4:'K',  5:'B',  6:'N',  7:' ', 
         8:'P',  9:'P', 10:'P', 11:' ', 12:'P', 13:'P', 14:'P', 15:' ',
        16:' ', 17:' ', 18:' ', 19:'P', 20:' ', 21:' ', 22:' ', 23:'R',
        24:' ', 25:' ', 26:' ', 27:' ', 28:' ', 29:' ', 30:' ', 31:'P',
        32:'p', 33:' ', 34:' ', 35:' ', 36:' ', 37:' ', 38:' ', 39:' ',
        40:' ', 41:'r', 42:' ', 43:'p', 44:' ', 45:' ', 46:' ', 47:' ',
        48:' ', 49:'p', 50:'p', 51:' ', 52:'p', 53:'p', 54:'p', 55:'p',
        56:' ', 57:'n', 58:'b', 59:'q', 60:'k', 61:'b', 62:'n', 63:'r'}'''
    try:
        assert c.vertical_travel(41,33) == True
        assert c.vertical_travel(41,1) == False
        assert c.vertical_travel(41,57) == False
        assert c.vertical_travel(23,39) == False
        assert c.vertical_travel(23,7) == True
        return True
    except:
        return False

def test_diagonal_travel():
    # Test diagonal movement, previous functions have validated the movement is only diagonal on the board
    c = Chessboard()
    c.move_piece(52,44)     # p to E3
    c.move_piece(11,19)     # P to D6
    c.move_piece(61,34)     # b to C4
    c.move_piece(2,29)      # B to F5
    '''{ 0:'R',  1:'N',  2:' ',  3:'Q',  4:'K',  5:'B',  6:'N',  7:'R', 
         8:'P',  9:'P', 10:'P', 11:' ', 12:'P', 13:'P', 14:'P', 15:'P',
        16:' ', 17:' ', 18:' ', 19:'P', 20:' ', 21:' ', 22:' ', 23:' ',
        24:' ', 25:' ', 26:' ', 27:' ', 28:' ', 29:'B', 30:' ', 31:' ',
        32:' ', 33:' ', 34:'b', 35:' ', 36:' ', 37:' ', 38:' ', 39:' ',
        40:' ', 41:' ', 42:' ', 43:' ', 44:'p', 45:' ', 46:' ', 47:' ',
        48:'p', 49:'p', 50:'p', 51:'p', 52:' ', 53:'p', 54:'p', 55:'p',
        56:'r', 57:'n', 58:'b', 59:'q', 60:'k', 61:' ', 62:'n', 63:'r'}'''
    try:
        assert c.diagonal_travel(34,16,9) == True     # b to A6
        assert c.diagonal_travel(34,6,7) == False     # b to G8
        assert c.diagonal_travel(29,57,7) == False    # B to B2
        assert c.diagonal_travel(29,46,9) == True     # B to H3
        return True
    except:
        return False

def test_rookValidity():
    c = Chessboard()
    c.move_piece(48,32)     # p to A4
    c.move_piece(15,31)     # P to H5
    c.move_piece(56,40)     # r to A3
    c.move_piece(7,23)      # R to H6
    c.move_piece(51,43)     # p to D3
    c.move_piece(11,19)     # P to D6
    '''{ 0:'R',  1:'N',  2:'B',  3:'Q',  4:'K',  5:'B',  6:'N',  7:' ', 
         8:'P',  9:'P', 10:'P', 11:' ', 12:'P', 13:'P', 14:'P', 15:' ',
        16:' ', 17:' ', 18:' ', 19:'P', 20:' ', 21:' ', 22:' ', 23:'R',
        24:' ', 25:' ', 26:' ', 27:' ', 28:' ', 29:' ', 30:' ', 31:'P',
        32:'p', 33:' ', 34:' ', 35:' ', 36:' ', 37:' ', 38:' ', 39:' ',
        40:'r', 41:' ', 42:' ', 43:'p', 44:' ', 45:' ', 46:' ', 47:' ',
        48:' ', 49:'p', 50:'p', 51:' ', 52:'p', 53:'p', 54:'p', 55:'p',
        56:' ', 57:'n', 58:'b', 59:'q', 60:'k', 61:'b', 62:'n', 63:'r'}'''
    try:
        assert c.rookValidity(40,41) == True        # move to the side
        assert c.rookValidity(40,44) == False       # try to jump over p
        assert c.rookValidity(40,48) == True        # go back one square
        assert c.rookValidity(40,33) == False       # try going diagonally
        assert c.rookValidity(40,39) == False       # try going off board to the side
        return True
    except:
        return False

def test_bishopValidity():
    c = Chessboard()
    c.move_piece(51,35)     # p to D4
    c.move_piece(58,37)     # b to F4
    '''{ 0:'R',  1:'N',  2:'B',  3:'Q',  4:'K',  5:'B',  6:'N',  7:'R', 
         8:'P',  9:'P', 10:'P', 11:'P', 12:'P', 13:'P', 14:'P', 15:'P',
        16:' ', 17:' ', 18:' ', 19:' ', 20:' ', 21:' ', 22:' ', 23:' ',
        24:' ', 25:' ', 26:' ', 27:' ', 28:' ', 29:' ', 30:' ', 31:' ',
        32:' ', 33:' ', 34:' ', 35:'p', 36:' ', 37:'b', 38:' ', 39:' ',
        40:' ', 41:' ', 42:' ', 43:' ', 44:' ', 45:' ', 46:' ', 47:' ',
        48:'p', 49:'p', 50:'p', 51:' ', 52:'p', 53:'p', 54:'p', 55:'p',
        56:'r', 57:'n', 58:' ', 59:'q', 60:'k', 61:'b', 62:'n', 63:'r'}'''
    try:
        assert c.bishopValidity(37,45) == False     # move vertically
        assert c.bishopValidity(37,36) == False     # move horizontally
        assert c.bishopValidity(37,23) == True      # move diagonally
        assert c.bishopValidity(37,1) == False      # jump over piece
        assert c.bishopValidity(37,10) == True      # kill P
        return True
    except:
        return False

def test_queenValidity():
    c = Chessboard()
    c.move_piece(52,36)     #p to E4
    c.move_piece(11,27)     #P to D5
    c.move_piece(59,49)     #q to F3
    c.move_piece(3,19)      #Q to D6
    '''{ 0:'R',  1:'N',  2:'B',  3:'Q',  4:'K',  5:'B',  6:'N',  7:'R', 
         8:'P',  9:'P', 10:'P', 11:' ', 12:'P', 13:'P', 14:'P', 15:'P',
        16:' ', 17:' ', 18:' ', 19:' ', 20:' ', 21:' ', 22:' ', 23:' ',
        24:' ', 25:' ', 26:' ', 27:'P', 28:' ', 29:' ', 30:' ', 31:' ',
        32:' ', 33:' ', 34:' ', 35:' ', 36:'p', 37:' ', 38:' ', 39:' ',
        40:' ', 41:' ', 42:' ', 43:' ', 44:' ', 45:'q', 46:' ', 47:' ',
        48:'p', 49:'p', 50:'p', 51:'p', 52:' ', 53:'p', 54:'p', 55:'p',
        56:'r', 57:'n', 58:'b', 59:' ', 60:'k', 61:'b', 62:'n', 63:'r'}'''
    try:
        assert c.queenValidity(3,19) == True    # move Q two forward
        assert c.queenValidity(3,5) == False    # try jumping over piece
        assert c.queenValidity(45,39) == False  # try going off the side
        assert c.queenValidity(45,31) == True   # move diagonally
        assert c.queenValidity(45,28) == False  # move like a (k)night
        return True
    except:
        return False

def test_kingValidity():
    c = Chessboard()
    c.move_piece(52,36)     #p to E4
    c.move_piece(11,27)     #P to D5
    c.move_piece(59,49)     #q to F3
    c.move_piece(3,19)      #Q to D6
    c.move_piece(4,31)      #K to H5 (lil cheat)
    
    '''{ 0:'R',  1:'N',  2:'B',  3:'Q',  4:' ',  5:'B',  6:'N',  7:'R', 
         8:'P',  9:'P', 10:'P', 11:' ', 12:'P', 13:'P', 14:'P', 15:'P',
        16:' ', 17:' ', 18:' ', 19:' ', 20:' ', 21:' ', 22:' ', 23:' ',
        24:' ', 25:' ', 26:' ', 27:'P', 28:' ', 29:' ', 30:' ', 31:'K',
        32:' ', 33:' ', 34:' ', 35:' ', 36:'p', 37:' ', 38:' ', 39:' ',
        40:' ', 41:' ', 42:' ', 43:' ', 44:' ', 45:'q', 46:' ', 47:' ',
        48:'p', 49:'p', 50:'p', 51:'p', 52:' ', 53:'p', 54:'p', 55:'p',
        56:'r', 57:'n', 58:'b', 59:' ', 60:'k', 61:'b', 62:'n', 63:'r'}'''
    try:
        assert c.kingValidity(60,52) == True   # move k one forward
        assert c.kingValidity(31,32) == False  # try going off the side
        assert c.kingValidity(60,59) == True   # move to the side
        assert c.kingValidity(31,22) == True   # move diagonally
        assert c.kingValidity(31,38) == True  # move diagonally
        assert c.kingValidity(31,37) == False  # move weirdly
        return True
    except:
        return False

print("Testing create_board():     ", test_create_board())
print("Testing current_board():    ",test_current_board())
print("Testing reveal_piece():     ", test_reveal_piece())
print("Testing valid_input():      ", test_valid_input())
print("Testing same_team:          ", test_same_team())
print("Testing move_pieces():      ", test_move_pieces())
print("Testing horizontal_travel():", test_horizontal_travel())
print("Testing vertical_travel():  ", test_vertical_travel())
print("Testing diagonal_travel():  ", test_diagonal_travel())
print("Testing rookValidity():    ", test_rookValidity())
print("Testing bishopValidity():", test_bishopValidity())
print("Testing queenValidity():", test_queenValidity())
print("Testing kingValidity():", test_kingValidity())