import math

def paint_calc(height, width, cover):
  number_of_cans = (test_h * test_w) / coverage
  cans = math.ceil(number_of_cans)
  print(f"You'll need {cans} cans of paint.")

test_h = int(input()) # Height (m)
test_w = int(input()) # Width (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)