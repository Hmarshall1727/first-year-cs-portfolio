string = "Hansa Rostock is the best football team in the world. Dynamo Dresden is the worst football team in the world."
spaces = len([x for x in string if x == ' '])
stops = len([x for x in string if x == '.'])
print(f"Hansa Rostock is the best football team in the world. Dynamo Dresden is the worst football team in the world.")
print(f"There are {spaces} spaces in this string.")
print(f"There are {stops} full stops in this string.")
