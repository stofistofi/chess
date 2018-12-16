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
        if (lower_case and self.__board[input].islower()):
            return True
        elif (not lower_case and self.__board[input].isupper()): 
            return True
        else: 
            return False

    def horizontal_travel(self, move, destination):
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
        # check pieces on path, OK if one piece at the end
        for h in range(0, len(horizontal_move)):
            if horizontal_move[h] != " ":
                #print(horizontal_move[h])
                return False
        return True

    def vertical_travel(self, move, destination):
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
            # check pieces on path, OK if one piece at the end
            for v in range(0, len(vertical_move)):
                if vertical_move[v] != " ":
                    return False
            return True

    def rookValidity(self, move, destination):
        # Rooks traveling vertically should always be on square coordinates modulus 8 of original position.
        diff = abs(move-destination)
        # Rooks traveling horizontally should always be between most left and most right squares (inclusive) on line.
        # vertical finds position from leftside, horizon0 and horizon1 determines interval
        vertical = move % 8
        horizon0 = move - vertical
        horizon1 = horizon0 + 7
        if (horizon0 <= destination <= horizon1):
            if self.horizontal_travel(move, destination):
                return True
            else:
                return False
        elif (diff % 8 == 0):
            if self.vertical_travel(move, destination):
                return True
        else:
            return False

    def diagonal_travel(self, move, destination, degree):
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
                if abs(move - s) % degree == 0:
                    diagonal_move.append(self.reveal_piece(s))
            # check pieces on path, OK if one piece at the end
            for d in range(0, len(diagonal_move)):
                if diagonal_move[d] == 'K' or diagonal_move[d] == 'k':
                    print("Check!")
                if diagonal_move[d] != " ":
                    return False
            # if none found:
            return True

    def bishopValidity(self, move, destination):
        diff = abs(move-destination)
        # some cool discrete mathematics, ala Halldór Halldórsson, reveals that diagonal movements 
        # should always either have a length of 7s (/) or 9s (\)
        if (diff % 7 == 0):
            if self.diagonal_travel(move, destination, 7):
                return True
            else:
                return False
        elif (diff % 9 == 0):
            if self.diagonal_travel(move, destination, 9):
                return True
            else:
                return False
        else:
            return False

    def queenValidity(self, move, destination):
        if self.rookValidity(move, destination) or self.bishopValidity(move, destination):
            return True
        else:
            return False

    def kingValidity(self, move, destination):
        diff = destination-move
        # going off left side
        if (move % 8 == 0) and (diff == -1):
            return False
        elif ((move+1) % 8 == 0) and (diff == 1):
            return False
        elif abs(diff) == 1 or 7 <= abs(diff) <= 9:
            return True
        
        #Castling
        elif move == 60 and destination == 62 and 'r' == self.reveal_piece(63) and ' ' == self.reveal_piece(62) and ' ' == self.reveal_piece(61):
            self.__board[63] = ' '
            self.__board[61] = 'r'
            print("castliing")
            return True
        elif move == 60 and destination == 58 and 'r' == self.reveal_piece(56) and ' ' == self.reveal_piece(59) and ' ' == self.reveal_piece(58) and ' ' == self.reveal_piece(57):
            self.__board[56] = ' '
            self.__board[59] = 'r'
            print("castling")
            return True
        
        elif move == 4 and destination == 6 and 'R' == self.reveal_piece(7) and ' ' == self.reveal_piece(5) and ' ' == self.reveal_piece(6):
            self.__board[7] = ' '
            self.__board[5] = 'R'
            print("castling")
            return True
        
        elif move == 4 and destination == 2 and 'R' == self.reveal_piece(0) and ' ' == self.reveal_piece(1) and ' ' == self.reveal_piece(2) and ' ' == self.reveal_piece(3):
            self.__board[0] = ' '
            self.__board[3] = 'R'
            print("castling")
            return True
        else:

            return False

    def pawnValidity(self, name, move, destination, board):

        #if the pawn is in the initial state
        initialStateLower = [48, 49, 50, 51, 52, 53, 54, 55]
        initialStateHigher = [8, 9, 10, 11, 12, 13, 14, 15]
        if name.islower():
            
            if 'K' == board[destination - 7] or 'K' == board[destination - 9]:
                print("lower pawn has checked")
            #moving on top of pieces from initial state
            if move in initialStateLower:
                if move - 8 == destination:
                    if ' ' == board[destination]:
                        return True
                if move - 16 == destination:
                    if ' ' == board[destination] and ' ' == board[destination + 8]:
                        return True
                
            #killing initl state
            if ' ' != board[destination] and (move - 6 == destination or move - 9 == destination):
                return True

            #moving on top of pieces not initial state
            if move not in initialStateLower:
                if move - 8 == destination:
                    if ' ' == board[destination]:
                        return True

            #Killing a piece (Death by Pawn)
            if move - 7 == destination or move - 9 == destination:
                if ' ' != board[destination]:
                    return True
            else:
                return False
        elif name.isupper():

            if 'k' == board[destination - 7] or 'k' == board[destination - 9]:
                print("lower pawn has checked")
            
            #moving on top of pieces from initial state
            if move in initialStateHigher:
                if move + 8 == destination:
                    if ' ' == board[destination]:
                        return True
                if move + 16 == destination:
                    if ' ' == board[destination] and ' ' == board[destination - 8]:
                        return True
                else: return False
            
            #moving on top of pieces not initial state
            if move not in initialStateHigher:
                if move + 8 == destination:
                    if ' ' == board[destination]:
                        return True
            
            #Killing a piece (Death by Pawn)
            if move + 7 == destination or move + 9 == destination:
                if ' ' != board[destination]:
                    return True
            else:
                return False

    def knightValidity(self, name, move, destination, board):
        safeZone = [18,19,20,21,26,27,28,29,34,25,26,27,42,43,44,45]
        outBound1 = [58,59,60,61]
        outBound1plus2 = [57,58,59,60,61,62]
        outbound2 = [40,32,24,16]
        outbound2plus2 = [48,40,32,24,16,8]
        outbound3 = [2,3,4,5]
        outbound3plus2 = [1,2,3,4,5,6]
        outbound4 = [23,31,39,47]
        outbound4plus2 = [15,23,31,39,47,55]
        redzone1 = [10,11,12,13]
        redzone1v1 = [9,10,11,12,13,14]
        redzone2 = [50,51,52,53]
        redzone2v2 = [49,50,51,52,53,54]
        redzone3 = [17,25,33,41,49]
        redzone4 = [22,30,38,46]

        #shortcuts
        d = destination
        forl = move - 17
        forr = move - 15
        lef = move - 10
        led = move + 6
        dol = move + 15
        dor = move + 17
        rif = move - 6
        rid = move + 10

        #knight checking king?
        #if 'K' == self.reveal_piece()

        #if the move is from the safe zone
        if move in safeZone and (lef == d or rif == d or rid == d or led == d or forl == d or forr == d or dor == d or dol == d):
            return True
        if move in outBound1plus2:
            if forl == d or forr == d:
                return True
            if move in outBound1:
                if lef == d or rif == d:
                    return True
        
        #corner cases
        if move == 56 and (forr == d or rif == d):
            return True
        if move == 63 and (forl == d or lef == d):
            return True
        if move == 0 and (dor == d or rid == d):
            return True
        if move == 7 and (dol == d or led == d):
            return True
        if move == 48 and (forr == d):
            return True
        if move == 57 and (rif == d):
            return True
        if move == 62 and (forr == d):
            return True
        if move == 55 and (forl == d):
            return True
        if move == 8 and (dor == d):
            return True
        if move == 1 and (rid == d):
            return True
        if move == 6 and (led == d):
            return True
        
        #redzone corner cases
        if move == 9 and (rif == d or rid == d):
            return True
        if move == 14 and (lef == d or led == d):
            return True
        if move == 49 and (rif == d or rid == d):
            return True
        if move == 54 and (lef == d or led == d):
            return True
        
        #edge of board cases
        if move in outbound2plus2:
            if rid == d or rif == d:
                return True
            if move in outbound2:
                if dor == d or forr == d:
                    return True
        if move in outbound3plus2:
            if dor == d or dol == d:
                return True
            if move in outbound3:
                if led == d or rid == d:
                    return True
        if move in outbound4plus2:
            if lef == d or led == d:
                return True
            if move in outbound4:
                if forl == d or dol == d:
                    return True
            
            #red zone
            if move in redzone1v1:
                if dol == d or dor == d:
                    return True
                if move in redzone1:
                    if rid == d or led == d or lef == d or rif == d:
                        return True
            
            if move in redzone2v2:
                if forl == d or forr == d:
                    return True
                if move in redzone2:
                    if lef == d or led == d or rif == d or rid == d:
                        return True

            if move in redzone3:
                if forl == d or forr == d or dol == d or dor == d or rif == d or rid == d:
                    return True

            if move in redzone4:
                if forl == d or forr == d or lef == d or led == d or dol == d or dor == d:
                    return True
        else:
            return False

    def check_check(self, kingdex, boardStatus, turn):
        if turn == True:
            for i in range(0,64):
                if self.pawnValidity('p', i, kingdex, boardStatus):
                    print("UPPER King checked")
                    return True
        if turn == False:
            for i in range(0,64):
                if self.pawnValidity('P', i, kingdex, boardStatus):
                    print("lower king checked")
                    return True

    def valid_piece_move(self, lower_case, move, destination, currBoard):
        validPieceMove = False
        while (validPieceMove is False):

            if (self.reveal_piece(move).lower() == 'p'): 
                if (self.pawnValidity(self.reveal_piece(move), move, destination, self.current_board())):
                    validPieceMove = True
                else:
                    return False

            if (self.reveal_piece(move).lower() == 'n'): 
                if (self.knightValidity(self.reveal_piece(move), move, destination, self.current_board())):
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

    def find_king(self, lower_case):
        if lower_case:
            find = 'K'
            for i in range(0, 64):
                if (self.reveal_piece(i) == find):
                    s = self.reveal_piece(i)
                    return s
                else:
                    s = 100
        else:
            find = 'k'
            for i in range(0, 64):
                if (self.reveal_piece(i) == find):
                    s = self.reveal_piece(i)
                    return s
                else:
                    s = 200
        return s

           

    # def find_kingEscapes(self, lower_case):
    #     king = self.find_king(lower_case)
    #     kingsEscapes = []
    #     if self.valid_piece_move(lower_case, king, king+1, self.current_board()):
    #         kingsEscapes.append(king+1)
    #     elif self.valid_piece_move(lower_case, king, king-1, self.current_board()):
    #         kingsEscapes.append(king-1)
    #     for k in range(7,10):
    #         if self.valid_piece_move(lower_case, king, king+k, self.current_board()):
    #             kingsEscapes.append(king+k)
    #     for k in range(-9,-6):
    #         if self.valid_piece_move(lower_case, king, king+k, self.current_board()):
    #             kingsEscapes.append(king+k)
    #     return kingsEscapes

    # def check(self, lower_case, move):
    #     # after moving a piece we check if the piece has checked the opponent's king
    #     # we do this by reusing valid_piece_move but for the piece's new location and the location of the other's king
    #     # let's find the king
    #     print("checking check")
    #     king = self.find_king(lower_case)
    #     # let's see if moving from the new location to the king would be a legal move, if so, it's check
    #     if (self.valid_piece_move(lower_case, move, king, self.current_board())):
    #         print("Check!!!")
    #         return True
    #     else:
    #         return False

    # def checkmate(self, lower_case):
    #     king = self.find_king(lower_case)
    #     kingsEscapes = self.find_kingEscapes(lower_case)
    #     if len(kingsEscapes) == 0:
    #         return True
    #     for k in kingsEscapes:
    #         for p in self.current_board():
    #             if self.valid_piece_move(lower_case, p, king, self.current_board()):
    #                 kingsEscapes = kingsEscapes.remove(k)
    #     if len(kingsEscapes) == 0:
    #         return True
    #     else:
    #         return False

    def ask_for_input(self, lower_case, output):
        if (lower_case): 
            print("\nlower case ", output)
        else:
            print("\nUPPER CASE ", output)

def main():
    ### TODO 'clear' vs. 'clr'
    ### TODO Refractor
    ### TODO Test script
    ### TODO Check and checkmate are unstable
    os.system('clear')
    c = Chessboard()
    print(str(c))
    lower_case = False     # 0: White, lower, 1: Black, UPPER
    game = True            # 1: in game, 0: game over

    while (game):    
    # while game is on
    # toggle player
        lower_case = not lower_case

        validPlay = False
        while (validPlay == False):        
        # while the play is not valid
            m = 0

            validMove = False
            while (validMove == False):
            # while piece selected to move is not valid
                # valid_input checks string to see whether it's on the board (e.g. 'D5' OK, not 'Z9')
                # same_team checks whether player's selected own team (and thereby not the other's or an empty square)
                os.system('clear')
                print(str(c))
                c.ask_for_input(lower_case, "Move:")
                move = input()                  # E.g. 'C2'
                if (c.valid_input(move) and c.same_team(lower_case, move_alg(move))):
                    m = move_alg(move)          # 50
                    validMove = True
                else:
                    print("Invalid selection")

            #if (c.check( lower_case, m)):
            #    print("check!!")


            validDestination = False
            while (validDestination == False):
            # while destination is not valid
                c.ask_for_input(lower_case, "Destination:")
                destination = input()         # E.g. 'C4'
                # Move piece and destination piece can't be the same team
                # Check if the play is legal

                if (c.find_king( lower_case)):
                    print("Warning: ")

                if (c.valid_input(destination) and not c.same_team(lower_case, move_alg(destination)) and c.valid_piece_move(lower_case, m, move_alg(destination), c.current_board())):
                    validDestination = True
                    d = move_alg(destination)  # 34
                    c.move_piece(m, d)

                    validPlay = True
                else:
                    print("Invalid move!")
                    break
        os.system('clear')
        print(str(c))

        
        if (c.find_king(lower_case)) == 100:
            print("king dead - lower Wins!!")
            game = not game
            break
        elif (c.find_king(lower_case)) == 200:
            print("king dead - UPPER Wins!!")
            game = not game
            break
    print("game ended")
main()

# this is the newest version