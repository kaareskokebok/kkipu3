from random import random

treff = 0.9

for i in range(100):
  if random() < treff:
    print("treff")
  else:
    print("bom")