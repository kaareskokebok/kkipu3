fart = 6.5  # 6,5 km/t
print("Oppgi avstanden på kartet (i cm):")
avstand_kart_cm = float(input())

avstand_terreng_cm = avstand_kart_cm * 20000
avstand_terreng_m = avstand_terreng_cm / 100
avstand_terreng_km = avstand_terreng_m / 1000
tid_timer = avstand_terreng_km / fart
tid_minutter = round(tid_timer * 60)
print(f"Avstand i terrenget: {avstand_terreng_km} km")
print(f"Tid brukt på denne etappen: {tid_minutter} min")