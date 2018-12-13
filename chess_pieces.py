
#Basic forward passive pawn moves
def pawnValidity(name, fromm, destination, board):

    #if the pawn is in the initial state
    initialStateLower = [48, 49, 50, 51, 52, 53, 54, 55]
    initialStateHigher = [8, 9, 10, 11, 12, 13, 14, 15]

    #check if its lower
    if name.islower():
        #print('its so small!!')
        #moving on top of pieces from initial state
        if fromm in initialStateLower:
            if fromm - 8 == destination:
                if ' ' == board[destination]:
                    print("solid 1 forward move")
                    return True
            if fromm - 16 == destination:
                if ' ' == board[destination] and ' ' == board[destination+ 8]:
                    print("Solid 2 forward move")
                    return True
            else: return False
        
        #moving on top of pieces not initial state
        if fromm not in initialStateLower:
            if fromm - 8 == destination:
                if ' ' != board[destination]:
                    print("solid 1 forward move")
                    return True
        
        #Killing a piece (Death by Pawn)
        if fromm - 7 == destination or fromm - 9 == destination:
            if ' ' != board[destination]:
                print("You just Killed")
                return True
        else:
            print("need to work on this edge case small")
            return False
    ###################################################################################################################upper starts here
    elif name.isupper():
        #moving on top of pieces from initial state
        if fromm in initialStateHigher:
            if fromm + 8 == destination:
                if ' ' == board[destination]:
                    print("solid 1 forward move")
                    return True
            if fromm + 16 == destination:
                if ' ' == board[destination] and ' ' == board[destination - 8]:
                    print("Solid 2 forward move")
                    return True
            else: return False
        
        #moving on top of pieces not initial state
        if fromm not in initialStateHigher:
            if fromm + 8 == destination:
                if ' ' != board[destination]:
                    print("solid 1 forward move")
                    return True
        
        #Killing a piece (Death by Pawn)
        if fromm + 7 == destination or fromm + 9 == destination:
            if ' ' != board[destination]:
                print("You just Killed" + board[destination])
                return True
        else:
            print("need to work on this edge case BIG")
            return False


def knightValidity(name, fromm, destination, board):
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
    forl = fromm - 17
    forr = fromm - 15
    lef = fromm - 10
    led = fromm + 6
    dol = fromm + 15
    dor = fromm + 17
    rif = fromm - 6
    rid = fromm + 10

    if name.islower() or name.isupper():
        #if the move is from the safe zone
        if fromm in safeZone and (lef == d or rif == d or rid == d or led == d or forl == d or forr == d or dor == d or dol == d):
            return True
        if fromm in outBound1plus2:
            if fromm - 17 == d or forr == d:
                return True
            if fromm in outBound1:
                if lef == d or rif == d:
                    return True
        #corner cases
        if fromm == 56 and (forr == d or rif == d):
            return True
        if fromm == 63 and (forl == d or lef == d):
            return True
        if fromm == 0 and (dor == d or rid):
            return True
        if fromm == 7 and (dol == d or led == d):
            return True
        if fromm == 48 and (forr == d):
            return True
        if fromm == 57 and (rif == d):
            return True
        if fromm == 62 and (forr == d):
            return True
        if fromm == 55 and (forl == d):
            return True
        if fromm == 8 and (dor == d):
            return True
        if fromm == 1 and (rid == d):
            return True
        if fromm == 6 and (led == d):
            return True
        
        #redzone corner cases
        if fromm == 9 and (rif == d or rid == d):
            return True
        if fromm == 14 and (lef == d or led == d):
            return True
        if fromm == 49 and (rif == d or rid == d):
            return True
        if fromm == 54 and (lef == d or led == d):
            return True
        
        #edge of board cases
        if fromm in outbound2plus2:
            if rid == d or rif == d:
                return True
            if fromm in outbound2:
                if dor == d or forr == d:
                    return True
        if fromm in outbound3plus2:
            if dor == d or dol == d:
                return True
            if fromm in outbound3:
                if led == d or rid == d:
                    return True
        if fromm in outbound4plus2:
            if lef == d or led == d:
                return True
            if fromm in outbound4:
                if forl == d or dol == d:
                    return True
            
            #red zone
            if fromm in redzone1v1:
                if dol == d or dor == d:
                    return True
                if fromm in redzone1:
                    if rid == d or led == d or lef == d or rif == d:
                        return True
            
            if fromm in redzone2v2:
                if forl == d or forr == d:
                    return True
                if fromm in redzone2:
                    if lef == d or led == d or rif == d or rid == d:
                        return True
            if fromm in redzone3:
                if forl == d or forr == d or dol == d or dor == d or rif == d or rid == d:
                    return True
            if fromm in redzone4:
                if forl == d or forr == d or lef == d or led == d or dol == d or dor == d:
                    return True
        else:
            print('caught a false move!')
            return False

            
#bridge for knight

###########################################################
def validator(name, fromm, destination, boardStatus, turn):
    if name == 'p' or name =='P':
        print("pawn being validated")
        if pawnValidity(name, fromm, destination, boardStatus):
            print("done")
            return True
    if name == 'n' or name =='N':
        if knightValidity(name, fromm, destination, boardStatus):
            return True

def main():



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




     # check for normal moves forward by 1 and fromm + 8 == destination
    #     if fromm in lastForHigher and fromm - 8 == destination:
    #         print("Invalid move 1forward")
    #         return False
        
    #     # if the pawns are in the last row of their opponennt side
    #     if fromm  in lastForHigher and fromm + 8 == destination:
    #         print("Invalid move 1forward")
    #         return False

    #     #check if the pawn is on the edge
    #     if fromm % 8 == 0 and destination == fromm + 7 or ((fromm + 1) % 8 == 0 and destination == fromm - 7):
    #         print('illegal Kill move!')
    #         return False
        
    #     #if the player wants to go forward by 1 or 2 in the initial stage #edit: also cant move over a piece
    #     if fromm in initialStateHigher and (fromm + 8 == destination or fromm + 16 == destination):
    #         if fromm + 16 == destination and ' ' !=  board.reveal_piece(destination + 8):
    #             print("cant move over pieces")
            
    #     # check if moving more than one
    #     if fromm in initialStateHigher and fromm - destination != fromm -8:
    #         print("has to move forward by one!")
    #         return False
        
    #     #check if pawn is moving on top of a piece
    #     if ' ' == board.reveal_piece(destination):
    #         print("valid destination")

    #     if ' ' !=  board.reveal_piece(destination) and  board.reveal_piece(destination).islower() or  board.reveal_piece(destination) == 'k':
    #         print("valid kill move ")
    #         return True
        
    #     #check if the pawn is on the edge
    #     if fromm % 8 == 0 and destination == fromm +7 or ((fromm + 1) % 8 == 0 and destination == fromm + 9):
    #         print('illegal Kill move!')
    #         return False
    #     elif ' ' != board.reveal_piece(destination):
    #         print('illigal move')
    #         return False
    # print("none of the if statements were hit so return true")
    # return True'''
#########################################################################################################################################################

#########################################################################################################################################################

    # # check for normal moves forward by 1 took out-> and ' ' == board.reveal_piece(destination)
    #     if fromm not in lastForLower and fromm not in initialStateLower and fromm - 8 != destination:
    #         print("Invalid move only 1 forward")
    #         return False
        
    #     # if the pawns are in the last row of their opponennt side
    #     if fromm in lastForLower and fromm - 8 == destination:
    #         print("Invalid move 1forward")
    #         return False
        
    #     #check if the pawn is on the edge
    #     if fromm % 8 == 0 and destination == fromm - 9 or ((fromm + 1) % 8 == 0 and destination == fromm - 7):
    #         print('illegal Kill move!')
    #         return False
        
    #     #if the player wants to go forward by 1 or 2 in the initial stage #edit: also cant move over a piece
    #     if fromm in initialStateLower and (fromm - 8 == destination or fromm - 16 == destination):
    #         if fromm - 16 == destination and ' ' !=  board.reveal_piece(destination - 8):
    #             print("cant move over pieces")
            
    #         # check if moving more than one
    #         if fromm in initialStateLower and (destination != fromm -8 or destination != fromm -16):
    #             print("has to move forward by one!")
    #             return False
    #         #check if pawn is moving on top of a piece or killing it
    #         if ' ' == board.reveal_piece(destination):
    #             print("valid destination")
    #             return True
        
    #     if ' ' !=  board.reveal_piece(destination) and  board.reveal_piece(destination).isupper() and  board.reveal_piece(destination) != 'K':
    #         print("valid kill move ")
    #         return True
    #     ###
    #     elif  ' ' !=  board.reveal_piece(destination) and  board.reveal_piece(destination).isupper() and  board.reveal_piece(destination) == 'K':
    #         print("killing the king?")
        
    #     else:
    #         print("thats a new move that I havent caught yet")
    #         return False

######## if the name is upper
    # elif name.isupper():
    #     print('its so Big!!')
    #     return True
       