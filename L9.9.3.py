def populasjon(aar):
  return 1500 * 0.88**aar

aaret = 0
while populasjon(aaret) >= 10:
  aaret += 1
print(aaret)  # Det tar 40 år
# print(populasjon(aaret))  # 9.02