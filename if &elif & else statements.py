is_Female=True
is_Thin= True

if is_Female:
  print("You are a female.")
else:
  print("You are not a female")

is_Female= False
is_Thin= False

if is_Female:
  print("You are a female.")
else:
  print("You are not a female.")

is_Female=True
is_Thin= True

if is_Female or is_Thin:#An example usage of the keyword called "or"
  print("You are a female or thin or both")
else:
  print("You are neither female nor thin")

if(is_Female and is_Thin):
  print("You are both female and thin")
else:
  print("You are not both female and thin")

is_Female= False
is_Thin= True

if(is_Female and is_Thin):#An example usage of the keyword called "and"
  print("You are both female and thin")
else:
  print("You are not both female and thin")


is_Female=True
is_Thin=False



if(is_Female and is_Thin):
  print("You are both female and thin")
elif is_Female and (not is_Thin):
  print("You are a fat female")
else:
  print("You are not both female and thin")