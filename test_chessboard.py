from chessboard import Chessboard

# def test_get_current_board():
#     expected_board = { 0:'R',  1:'N',  2:'B',  3:'Q',  4:'K',  5:'B',  6:'N',  7:'R', 
#                          8:'P',  9:'P', 10:'P', 11:'P', 12:'P', 13:'P', 14:'P', 15:'P',
#                         16:' ', 17:' ', 18:' ', 19:' ', 20:' ', 21:' ', 22:' ', 23:' ',
#                         24:' ', 25:' ', 26:' ', 27:' ', 28:' ', 29:' ', 30:' ', 31:' ',
#                         32:' ', 33:' ', 34:' ', 35:' ', 36:' ', 37:' ', 38:' ', 39:' ',
#                         40:' ', 41:' ', 42:' ', 43:' ', 44:' ', 45:' ', 46:' ', 47:' ',
#                         48:'p', 49:'p', 50:'p', 51:'p', 52:'p', 53:'p', 54:'p', 55:'p',
#                         56:'r', 57:'n', 58:'b', 59:'q', 60:' ', 61:'b', 62:'n', 63:'r'} 
#     c = Chessboard()
#     try:
#         assert c.current_board() == expected_board
#         return True
#     except:
#         return False

# print(test_get_current_board())


def test_move_piece():
    expected_board = { 0:'R',  1:'N',  2:'B',  3:'Q',  4:'K',  5:'B',  6:'N',  7:'R', 
                         8:'P',  9:'P', 10:' ', 11:'P', 12:'P', 13:'P', 14:'P', 15:'P',
                        16:' ', 17:' ', 18:' ', 19:' ', 20:' ', 21:' ', 22:' ', 23:' ',
                        24:' ', 25:' ', 26:'P', 27:' ', 28:' ', 29:' ', 30:' ', 31:' ',
                        32:' ', 33:' ', 34:' ', 35:' ', 36:' ', 37:' ', 38:' ', 39:' ',
                        40:'p', 41:' ', 42:' ', 43:' ', 44:' ', 45:' ', 46:' ', 47:' ',
                        48:' ', 49:'p', 50:'p', 51:'p', 52:'p', 53:'p', 54:'p', 55:'p',
                        56:'r', 57:'n', 58:'b', 59:'q', 60:'k', 61:'b', 62:'n', 63:'r'}
    c = Chessboard()
    c.move_piece(48,40)
    c.move_piece(10,26)
    #c.move_piece(40, 39) # fails
    try:
        assert c.current_board() == expected_board
        return True
    except:
        print(c.current_board())
        print(expected_board)
        return False

print(test_move_piece())