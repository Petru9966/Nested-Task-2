#asking for the type of the cover
print("What type of cover does this book have? Hard or soft?")
cover=input()
if (cover=="soft"):
  print("Is this book perfect bound? Yes or no?")
  bound=input()
  if (bound=="yes"):
    print("Soft cover, perfect bound books are very popular!")
  if(bound=="no"):
      print("Soft covers with coilsor stitches are great for short books!")
elif (cover=="hard"):
  print("Books with hard covers can be more expensive!")

