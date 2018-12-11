
def move_alg(inpu):
  inpu = inpu.upper()
  intValue1 = ord(inpu[0])
  intValue1 -= 65 
  intValue2 = int(inpu[1])
  return ((8 - intValue2) * 8) + intValue1

# 7-1 * 8 + A