print ("Your Daily Affirmations Generator 🤩")
name = input("Hello you amazing person. What is your name? ")

if name.upper() == "DAN":
  day = input("What is the day of the week? ")
  if day.lower() == "monday":
    print("Ahhh Monday. I know it's not your fave,", name.upper(), "but you can do this! New week, new", name.upper(), "! Have an awesome start to the week 💥")
  if day.lower() == "tuesday":
    print("Tuesday is here! Second day in", name.upper(), ", keep up the good work 💪")
  if day.lower() == "wednesday":
    print("Happy hump day", name.upper(), "! It's Wednesday! Halfway to the weekend, whoop whoop 🍻")
  if day.lower() == "thursday":
    print("Hey", name.upper(), "Thursday is like Friday, so you may as well start relaxing buddy 💅")
  if day.lower() == "friday":
    print(name.upper(), "! You made it! It's FRIDAY! FRIDAY! FRIDAY! FRIDAY! FRIDAY! FRIDAY! 🎊")
  if day.lower() == "saturday":
    print ("Why hello", name.upper(), ", what do you have planned for today? I hope you have a wonderful fulfilling time, whatever you do 🍻")
  if day.lower() =="sunday":
    print ("Go ahead and chill out, watch some NFL RedZone", name.upper(), ", you've earned it 😊")
  else: 
    print("That is some out-of-this-world day,", name.upper(), "but have a good one anyway :)")

elif name.upper() == "STEF":
  day = input("What is the day of the week? ")
  if day.lower() == "monday":
    print("It's Monday! So what will you achieve this week", name.upper(), "? Do your to-do list and power on through, you can do this", name.upper(), "! Have an awesome start to the week.")
  if day.lower() == "tuesday":
    print("Tuesday is here! Second day in,", name.upper(), ", keep up the good work ")
  if day.lower() == "wednesday":
    print("Happy hump day", name.upper(), "! It's Wednesday! Halfway to the weekend, whoop whoop 🍻 (not that it makes a difference to you, eh", name.upper(), "!")
  if day.lower() == "thursday":
    print("Hey", name.upper(), "you are doing a great job, keep on truckin' 💅")
  if day.lower() == "friday":
    print(name.upper(), "! You made it! It's FRIDAY! FRIDAY! FRIDAY! FRIDAY! FRIDAY! FRIDAY! 🎊")
  if day.lower() == "saturday":
    print ("Why hello", name.upper(), ", I hope you have a wonderful, stress-free day 🍻")
  if day.lower() =="sunday":
    print ("I know you have to do the ironing", name.upper(), ", but please take a break, you've earned it 😊")
  else:
    print("That is some out-of-this-world day,", name.upper(), "but have a good one anyway :)")
    

else:
  print("Umm sorry I don't know you. But have a blessed day anyway!")