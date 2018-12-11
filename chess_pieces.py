import chessboard
#Basic forward passive pawn moves
def pawnValidity(name, fromm, destination, board):
    
    #if the pawn is in the initial state
    initialStateLower = [48, 49, 50, 51, 52, 53, 54, 55]
    initialStateHigher = [8, 9, 10, 11, 12, 13, 14, 15]

    #last row for the pieces
    lastForLower = [0,1,2,3,4,5,6,7]
    lastForHigher = [56,57,58,59,60,61,62,63]
    
    #check if its lower
    if name.islower():
        print('its so small!!')
    # check for normal moves forward by 1
        if fromm not in lastForLower and fromm - 8 == destination and ' ' == board[destination] and destination :
            print("valid move 1 forward")
            return True
        
        # if the pawns are in the last row of their opponennt side
        if fromm in lastForLower and fromm - 8 != destination:
            print("Wrong, cant move there")
            return False
        
        #check if the pawn is on the edge
        if fromm % 8 == 0 and destination == fromm - 9 or ((fromm + 1) % 8 == 0 and destination == fromm - 7):
            print('illegal Kill move!')
            return False
        
        #if the player wants to go forward by 1 or 2 in the initial stage #edit: also cant move over a piece
        if fromm in initialStateLower and (fromm - 8 == destination or fromm - 16 == destination):
            if fromm - 16 == destination and ' ' != board[destination - 8]:
                print("cant move over pieces")
            else:
                print("initial move allowed")
      
            #check if pawn is moving on top of a piece or killing it
            if ' ' == board[destination]:
                print("valid destination")
                return True
        
        if ' ' != board[destination] and board[destination].isupper() and board[destination] != 'K':
            print("valid kill move ")
            return False
        elif  ' ' != board[destination] and board[destination].isupper() and board[destination] == 'K':
            print("killing the king?")
        else:
            print("thats a new move that I havent caught yet")
            return False

######## if the name is upper
    elif name.isupper():
        print('its so Big!!')
    
    # check for normal moves forward by 1
        if fromm not in lastForHigher and fromm not in initialStateHigher and fromm + 8 == destination:
            print("valid move 1forward")
        
        # cant move through last space
        elif fromm  in lastForHigher and fromm + 8 == destination:
            print("Wrong")
            return False
    
    #if the player wants to go forward by 1 or 2 in the initial stage #edit: also cant move over a piece
        if fromm in initialStateLower and (fromm + 8 == destination or fromm + 16 == destination):
            if fromm + 16 == destination and ' ' != board[destination + 8]:
                print("cant move over pieces")
            else:
                print("initial move allowed")
    
    #check if pawn is moving on top of a piece
        if ' ' == board[destination]:
            print("valid destination")

        if ' ' != board[destination] and board[destination].islower() or board[destination] == 'k':
            print("valid kill move ")
            return False

        else:
            print("cant kill your own pieces")
            return False
        
        #check if the pawn is on the edge
        if fromm % 8 == 0 and destination == fromm +7 or ((fromm + 1) % 8 == 0 and destination == fromm + 9):
            print('illegal Kill move!')
            return False
        elif ' ' != board[destination]:
            print('illigal move')
            return False

###########################################################
def validator(name, boardStatus, fromm, destination, turn):
    validity = True
    if name == 'p' or name =='P':
        print("thats a pawn!")
        if pawnValidity(name, fromm, destination, boardStatus):
            return pawnValidity(name, fromm, destination, boardStatus)
    else:
        return validity

def main():
    board = { 0:'R',  1:'N',  2:'B',  3:'Q',  4:'K',  5:'B',  6:'N',  7:'R', 
            8:' ',  9:'P', 10:'P', 11:'P', 12:'P', 13:'P', 14:'P', 15:'P',
            16:' ', 17:' ', 18:' ', 19:' ', 20:' ', 21:' ', 22:' ', 23:' ',
            24:' ', 25:' ', 26:' ', 27:' ', 28:' ', 29:' ', 30:' ', 31:' ',
            32:' ', 33:' ', 34:' ', 35:' ', 36:' ', 37:' ', 38:' ', 39:' ',
            40:' ', 41:' ', 42:' ', 43:' ', 44:' ', 45:' ', 46:' ', 47:' ',
            48:'p', 49:'p', 50:'p', 51:'p', 52:'p', 53:'p', 54:'p', 55:'p',
            56:' ', 57:'n', 58:'b', 59:'q', 60:'k', 61:'b', 62:'n', 63:'r'}

    validator('p',board , 48, 1, True)




main()


#check on En Passant? could implement later...

#Pawns: if inital position, forward 1 or 2 (if the Pawn can reach the end of his opponent then it will change into a queen)
#Rooks: (minimum 1, maximum 7) forward/backwards or lef/rigth
#Knights: 2 forward or backward 1 left or right, 2 left or right 1 forward or backward
#Bishop: minimum 1 diagonal, maximum 7 diagonally
#Queen: can adopt moves from rook+bishop
#King: minimum 1 and maximum 1. unless castling (castling is when the rook and the King swap places.
# This can only be done if no piece is checking the King or if the move could result in a check)

##Overall check if any pieces are in the way. so A general rule would be to check the availability on the chessboard, then 

# 8 - 15 and 48 - 55 initial start for pawns
                    #check if the pawn is on the left edge
#KILLING by PAWNS  fromm % 8 == 0 and destination == fromm - 7:

#destination in board and ' ' == board[destination] 

    # if name == 'r' or name =='R':
    #   if destination:
    #     return True
    # if name == 'n' or name =='N':
    #   if destination:
    #     return True
    # if name == 'b' or name =='B':
    #   if destination:
    #     return True
    # if name == 'q' or name =='Q':
    #   if destination:
    #     return True
    # if name == 'k' or name =='K':
    #   if destination:
    #     return True