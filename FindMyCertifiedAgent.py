area = input("Chose an area : (aleppo),(Damascus), or (sweida) \n")
if area.lower() == "aleppo" :
   print("You chose aleppo")
elif area.upper() == "ALEPPO" :
   print("You chose aleppo")
else :
  print(f" Sorry ,{area} is not an our list!")
