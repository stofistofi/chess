
def chess_move_alg():

  inpu = input()
  intValue1 = ord(inpu[0])
  intValue1 -= 65 
  intValue2 = int(inpu[1])
  returnVal = ((8 - intValue2) * 8) + intValue1
  print(returnVal)
chess_move_alg()

# 7-1 * 8 + A