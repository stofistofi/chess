
#To Do List
# can kill forward???
#lower case pawns
def lowerPawnValidity(name, move, destination, board):

    #if the pawn is in the initial state
    initialStateLower = [48, 49, 50, 51, 52, 53, 54, 55]
    initialStateHigher = [8, 9, 10, 11, 12, 13, 14, 15]
    if name.islower():
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



# #upper case pawns
# def upperPawnValidity(name, move, destination, board):
    
    
#     #moving on top of pieces from initial state
#     if move in initialStateHigher:
#         if move + 8 == destination:
#             if ' ' == board[destination]:
#                 return True
#         if move + 16 == destination:
#             if ' ' == board[destination] and ' ' == board[destination - 8]:
#                 return True
#         else: return False
    
#     #moving on top of pieces not initial state
#     if move not in initialStateHigher:
#         if move + 8 == destination:
#             if ' ' == board[destination]:
#                 return True
    
#     #Killing a piece (Death by Pawn)
#     if move + 7 == destination or move + 9 == destination:
#         if ' ' != board[destination]:
#             return True
#     else:
#         return False


def knightValidity(name, move, destination, board):
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

            


def check_check(kingdex, boardStatus, turn):
    if turn == True:
        for i in range(0,64):
            if lowerPawnValidity('p', i, kingdex, boardStatus):
                print("UPPER King checked")
                return True
    if turn == False:
        for i in range(0,64):
            if lowerPawnValidity('P', i, kingdex, boardStatus):
                print("lower king checked")
                return True

###########################################################
def validator(name, move, destination, boardStatus, turn):

    #if turn is true then lower is has the turn
    if name == 'p':
        print("pawn being validated")
        if lowerPawnValidity(name, move, destination, boardStatus):
            return True

    if name =='P':
        if upperPawnValidity(name, move, destination, boardStatus):
            return True
            
    if name == 'n' or name =='N':
        if knightValidity(name, move, destination, boardStatus):
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

#check:
# how to know if there is a check:
# K in the possible destination