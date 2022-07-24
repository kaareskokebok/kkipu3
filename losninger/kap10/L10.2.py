from random import choice

jenter = 0
gutter = 0

for i in range(1000):
  barn = choice(["gutt", "jente"])
  if barn == "jente":
    jenter += 1
  else:
    gutter += 1
    
print(jenter/gutter)  # Forholdet nærmer seg 1