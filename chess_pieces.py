
#To Do List
# can kill forward???
#lower case pawns
def lowerPawnValidity(name, fromm, destination, board):

    #if the pawn is in the initial state
    initialStateLower = [48, 49, 50, 51, 52, 53, 54, 55]

        #moving on top of pieces from initial state
    if fromm in initialStateLower:
        if fromm - 8 == destination:
            if ' ' == board[destination]:
                return True
        if fromm - 16 == destination:
            if ' ' == board[destination] and ' ' == board[destination + 8]:
                return True
        else: return False
    
    #moving on top of pieces not initial state
    if fromm not in initialStateLower:
        if fromm - 8 == destination:
            if ' ' == board[destination]:
                return True
    
    #Killing a piece (Death by Pawn)
    if fromm - 7 == destination or fromm - 9 == destination:
        if ' ' != board[destination]:
            return True
    else:
        return False


#upper case pawns
def upperPawnValidity(name, fromm, destination, board):
    initialStateHigher = [8, 9, 10, 11, 12, 13, 14, 15]
    
    #moving on top of pieces from initial state
    if fromm in initialStateHigher:
        if fromm + 8 == destination:
            if ' ' == board[destination]:
                return True
        if fromm + 16 == destination:
            if ' ' == board[destination] and ' ' == board[destination - 8]:
                return True
        else: return False
    
    #moving on top of pieces not initial state
    if fromm not in initialStateHigher:
        if fromm + 8 == destination:
            if ' ' == board[destination]:
                return True
    
    #Killing a piece (Death by Pawn)
    if fromm + 7 == destination or fromm + 9 == destination:
        if ' ' != board[destination]:
            return True
    else:
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


    #if the move is from the safe zone
    if fromm in safeZone and (lef == d or rif == d or rid == d or led == d or forl == d or forr == d or dor == d or dol == d):
        return True
    if fromm in outBound1plus2:
        if forl == d or forr == d:
            return True
        if fromm in outBound1:
            if lef == d or rif == d:
                return True
    #corner cases
    if fromm == 56 and (forr == d or rif == d):
        return True
    if fromm == 63 and (forl == d or lef == d):
        return True
    if fromm == 0 and (dor == d or rid == d):
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
        return False

            
#bridge for knight

###########################################################
def validator(name, fromm, destination, boardStatus, turn):
    if name == 'p':
        print("pawn being validated")
        if lowerPawnValidity(name, fromm, destination, boardStatus):
            return True

    if name =='P':
        if upperPawnValidity(name, fromm, destination, boardStatus):
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

