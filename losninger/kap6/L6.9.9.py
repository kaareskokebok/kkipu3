total_tid = 0.0
tid_per_km = 3.8

for i in range(42): 
  total_tid += tid_per_km
  tid_per_km += 0.1

total_tid_timer = total_tid/60
# Skriver ut og avrunder svarene
print(f"Tid i minutter: {round(total_tid, 1)}")
print(f"Tid i timer: {round(total_tid_timer, 1)}")