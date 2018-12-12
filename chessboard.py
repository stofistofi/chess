# initializes a chess board on a comand line interface (CLI)
import os
from move_alg import move_alg
from chess_pieces import validator

class Chessboard():
    def create_board(self):
        # the chess board is a dictionary, the keys are incrementing integers from 0 to 63,
        # the values are the chess players. This makes calculations easier
        self.__board = { 0:'R',  1:'N',  2:'B',  3:'Q',  4:'K',  5:'B',  6:'N',  7:'R', 
                         8:'P',  9:'P', 10:'P', 11:'P', 12:'P', 13:'P', 14:'P', 15:'P',
                        16:' ', 17:' ', 18:' ', 19:' ', 20:' ', 21:' ', 22:' ', 23:' ',
                        24:' ', 25:' ', 26:' ', 27:' ', 28:' ', 29:' ', 30:' ', 31:' ',
                        32:' ', 33:' ', 34:' ', 35:' ', 36:' ', 37:' ', 38:' ', 39:' ',
                        40:' ', 41:' ', 42:' ', 43:' ', 44:' ', 45:' ', 46:' ', 47:' ',
                        48:'p', 49:'p', 50:'p', 51:'p', 52:'p', 53:'p', 54:'p', 55:'p',
                        56:'r', 57:'n', 58:'b', 59:'q', 60:'k', 61:'b', 62:'n', 63:'r'}

    def __init__(self):
        # initially a chess board is created
        self.create_board()

    def __str__(self):
        # override the print function to print the board with guiding coordinates
        boardString = ""
        c = 8
        for b in self.__board:
            if (b % 8 == 0):
                boardString = boardString + '\n' + '(' + str(c) + ')  '         # numbers on the sides
                c -= 1
            boardString = boardString + '[' + self.__board[b] + ']'
        boardString = boardString + '\n \n' + '     (A)(B)(C)(D)(E)(F)(G)(H)'   # letters in the bottom
        return str(boardString)
    
    def move_piece(self, move, destination):
        # update board: destination value becomes the moved piece, slot of moved piece becomes empty
        self.__board[destination] = self.__board[move]
        self.__board[move] = " "

    def reveal_piece(self, key):
        # reveal_piece is useful for testing
        return self.__board[key]

    def current_board(self):
        # return the current chess board
        return self.__board
    
    def valid_input(self, input):
        return (len(input) == 2) and (64 < ord(input[:1].upper()) < 73) and (48 < ord(input[1:2]) < 57)

    def same_team(self, lower_case, input):
        i = move_alg(input)
        if (lower_case and self.__board[i].islower()):
            return True
        elif (not lower_case and self.__board[i].isupper()): 
            return True
        else: 
            return False

    def valid_move(self, lower_case, c):
        # boolean 'lower_case' determines if it's lower's turn
        validMove = False
        while (validMove is False):
            if (lower_case): print("\nlower case:")
            else: print("\nUPPER CASE:")
            print("\nMove:")
            move = input()
            if(self.valid_input(move) and (self.same_team(lower_case, move))):
                validMove = True
            os.system('clear')
            print(str(c))
        return move
    
    def valid_destination(self, lower_case, c):
        validDestination = False
        while (validDestination is False):
            if (lower_case): print("\nlower case:")
            else: print("\nUPPER CASE:")
            print("\nDestination:")
            destination = input()
            if(self.valid_input(destination) and not self.same_team(lower_case, destination)):
                validDestination = True
            os.system('clear')
            print(str(c))
        return destination
    
    def rookValidity(self, move, destination):
        # Rooks traveling vertically should always be on square coordinates modulus 8 of original position.
        diff = abs(move-destination)
        # Rooks traveling horizontally should always be between most left and most right squares (inclusive) on line.
        # vertical finds position from leftside, horizon0 and horizon1 determines interval
        # TODO don't jump over pieces
        vertical = move % 8
        horizon0 = move - vertical
        horizon1 = horizon0 + 7
        if (horizon0 <= destination <= horizon1):
            # if piece's moving horizontally, fill a list of the squares it's traversing, order of squares doesn't matter
            horizontal_move = []
            low_bound = 0
            hi_bound = 63
            if move < destination: 
                low_bound = move
                hi_bound = destination
            else: 
                low_bound = destination
                hi_bound = move
            for s in range(low_bound+1, hi_bound):      # e.g. from 27 to 32 (both exclusive)
                horizontal_move.append(self.reveal_piece(s))
            # check 
            print(horizontal_move)
            # check pieces on path, OK if one piece at the end
            for h in range(0, len(horizontal_move)):
                if horizontal_move[h] != " ":
                    print(horizontal_move[h])
                    return False
            return True

        elif (diff % 8 == 0):
            vertical_move = []
            low_bound = 0
            hi_bound = 63
            if move < destination: 
                low_bound = move
                hi_bound = destination
            else: 
                low_bound = destination
                hi_bound = move
            # similarly, for vertical movement we create a list of squares to check but we only add every eigth square
            for s in range(low_bound+1, hi_bound):
                if abs(move - s) % 8 == 0:
                    vertical_move.append(self.reveal_piece(s))
            # check
            print(vertical_move)
            # check pieces on path, OK if one piece at the end
            for v in range(0, len(vertical_move)):
                if vertical_move[v] != " ":
                    return False
            return True
        else:
            return False

    def bishopValidity(self, move, destination):
        diff = abs(move-destination)
        # some cool discrete mathematics, ala Halldór Halldórsson, reveals that diagonal movements 
        # should always either have a length of 7s (/) or 9s (\)
        if (diff % 7 == 0):
            # check squares in between
            diagonal_move = []
            low_bound = 0
            hi_bound = 63
            if move < destination: 
                low_bound = move
                hi_bound = destination
            else: 
                low_bound = destination
                hi_bound = move
            # For diagonal movement we create a list of squares to check but we only add every seventh square
            for s in range(low_bound+1, hi_bound):
                if abs(move - s) % 7 == 0:
                    diagonal_move.append(self.reveal_piece(s))
            # check
            print(diagonal_move)
            # check pieces on path, OK if one piece at the end
            for d in range(0, len(diagonal_move)):
                if diagonal_move[d] != " ":
                    return False
            return True
        elif (diff % 9 == 0):
            # check squares in between
            diagonal_move = []
            low_bound = 0
            hi_bound = 63
            if move < destination: 
                low_bound = move
                hi_bound = destination
            else: 
                low_bound = destination
                hi_bound = move
            # For diagonal movement we create a list of squares to check but we only add every seventh square
            for s in range(low_bound+1, hi_bound):
                if abs(move - s) % 9 == 0:
                    diagonal_move.append(self.reveal_piece(s))
            # check
            print(diagonal_move)
            # check pieces on path, OK if one piece at the end
            for d in range(0, len(diagonal_move)):
                if diagonal_move[d] != " ":
                    return False
            return True
        else:
            return False

    def queenValidity(self, move, destination):
        if self.rookValidity(move, destination) or self.bishopValidity(move, destination):
            return True
        else:
            return False

    def kingValidity(self, move, destination):
        diff = abs(move-destination)
        if diff == 1 or 7 <= diff <= 9:
            return True
        else:
            return False

    def valid_piece_move(self, lower_case, move, destination, currBoard):
        validPieceMove = False
        while (validPieceMove is False):
            if (self.reveal_piece(move).lower() == 'p'): 
                if validator(self.reveal_piece(move), move, destination, self.current_board(), lower_case):
                    validPieceMove = True
                else:
                    return False

            if (self.reveal_piece(move).lower() == 'r'):
                if (self.rookValidity(move, destination)):
                    validPieceMove = True
                else:
                    return False

            if (self.reveal_piece(move).lower() == 'b'):
                if (self.bishopValidity(move, destination)):
                    validPieceMove = True
                else:
                    return False

            if (self.reveal_piece(move).lower() == 'q'):
                if (self.queenValidity(move, destination)):
                    validPieceMove = True
                else:
                    return False

            if (self.reveal_piece(move).lower() == 'k'):
                if (self.kingValidity(move, destination)):
                    validPieceMove = True
                else:
                    return False
        return True

def main():
    ### TODO Spyrja út í 'clear' vs. 'clr'
    ### TODO Test script
    os.system('clear')
    c = Chessboard()
    print(str(c))
    lower_case = False       # 0: White, lower, 1: Black, UPPER
    status = 1               # 1: in game, 0: game over

    while (status == 1):    # while game is not won
        # toggle player
        lower_case = not lower_case

        while(True):    # while the input is correct
            # input move and destination and validate
            # output is the int of square in board (e.g. 0 for 'A1')
            move = move_alg(c.valid_move(lower_case, c))
            destination = move_alg(c.valid_destination(lower_case, c))
            # piece moved if valid
            piece = c.valid_piece_move(lower_case, move, destination, c.current_board())
            if (piece):
                c.move_piece(move, destination)
                os.system('clear')
                print(str(c))
                break
            else:
                print("Not a valid move.")

main()