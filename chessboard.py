# initializes a chess board on a comand line interface (CLI)

class Chessboard():
    def create_board(self):
        print("test")
        self.__board = {0:'R', 1:'K', 2:'B', 3:'Q', 4:'K', 5:'N', 6:'R', 7:'P', 8:'P', 9:'P', 10:'P', 11:'P', 12:'P', 13:'P', 14:'P'}

    def __init__(self):
        print("test1")
        self.create_board()
    
    def __str__(self):
        return str(self.__board)

def main():
    print('t')
    c = Chessboard()
    print(str(c))
    print('cc')

main()

'''
CLI:

(8)  [R][N][B][Q][K][B][N][R]
(7)  [P][P][P][P][P][P][P][P]
(6)  [ ][ ][ ][ ][ ][ ][ ][ ]
(5)  [ ][ ][ ][ ][ ][ ][ ][ ]
(4)  [ ][ ][ ][ ][ ][ ][ ][ ]
(3)  [ ][ ][p][ ][ ][ ][ ][ ]
(2)  [p][p][ ][p][p][p][p][p]
(1)  [r][n][b][q][k][b][n][r]

     (A)(B)(C)(D)(E)(F)(G)(H)

$ lower: c2 c4
$ UPPER: 
'''

'''
move(i, b):
    c2: 'p'
'''