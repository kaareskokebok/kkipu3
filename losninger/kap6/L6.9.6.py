summen = 0
tall = 1000
while tall > 10 ** (-15):  # Stopper når nytt ledd veldig lite
  summen += tall
  tall *= 0.9
print(summen)  # 10000