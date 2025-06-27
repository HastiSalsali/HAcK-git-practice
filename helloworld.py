print ("Hello, World!")
def median(input):
  input = sorted(input)
  medianVal = 0
  midPoint = math.floor(len(input) / 2)
  if len(input) % 2 == 0:
    a = input[midPoint - 1 ]
    b = input[midPoint]
    medianVal = (a + b) / 2
  else:
    medianVal = input[midPoint]
  return medianVal