print("""
FAKE FAN FINDER
----------------""")

band = input("Who is your favourite grunge band? ")
if band == "nirvana":
  print("Oh yeah? ")
  album = input("Name me the best album then... ")
  if album == "bleach":
    print("That is the correct answer, you really are a true fan.")
    song = input("So what's the best song on there?")
    if song == "love buzz":
      print("YES! Wow you are the ultimate fan")
    elif song == "dive":
      print("Truly an excellent song")
    else:
      print("I guess that's a good one")
  elif album == "insecticide":
      print("BUSTED! It's Incesticide you idiot")
  elif album =="incesticide":
      print("NICE.")
  elif album =="in utero":
      print("I concur.")
  elif album =="mtv unplugged":
      print("Niche! I like it.")
  elif album =="nevermind":
    print("Ugh that is such a rookie answer... I don't know if you're a true fan... ")
  else: 
    print("Fake fan!")
else:
  print("YOU ARE WRONG, NIRVANA IS THE ONLY GRUNGE BAND IN THE WORLD")