class Piece():
  
  print("hello1")
  def create_piece(self):
    print("hello2")
    self.__piece = ['name', 'color', 'status']

  def __init__(self):
    self.create_piece()
    
  def __str__(self):
    return str(self.__piece)


def main():
  print("hello Test")
  p = Piece()
  print(str(p))

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