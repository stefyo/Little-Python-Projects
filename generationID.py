print("Generation Identifier!")

year = int(input("What year were you born?"))

if year >= 1925 and year <= 1946:
  print("You are a Traditionalist.")
elif year >= 1947 and year <= 1964:
  print("Oh hey Baby Boomer.")
elif year >= 1965 and year <= 1981:
  print("Cooooool maaaaan, you are Gen X")
elif year >= 1982 and year <= 1995:
  print("Typical Millenial, bridging the gap between analogue and digital")
elif year >= 1996 and year <= 2015:
  print("You're a Gen Z baby!")
else:
  print("You are either to old or too young to be using a computer.")
