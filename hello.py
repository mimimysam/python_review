# int()
# float()
# bool()
# str()

# first = float(input("First: "))
# second = float(input("Second: "))
# sum = first + second
# print("Sum: " + str(sum))

temperature = 11
if temperature > 30:
  print("It's hot!")
elif temperature > 20:
  print("It's a nice day!")
elif temperature > 10:
  print("It's kinda cold!")
else:
  print("It's cooold!")

weight = int(input("weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
  converted = weight / 0.45
  print("Weight in lbs: " + str(converted))
else:
  converted = weight * 0.45
  print("Weight in kgs: " + str(converted))

i = 1
while i <= 3:
  print(i * '*')
  i += 1 # i = i + 1

names = ["Mimi", "Van", "Katie", "Eva"] # list
print(names[0:2]) # prints first 2 names

numbers = [1, 2, 3, 4, 5]
for item in numbers:
  print(item)

i = 0
while i < len(numbers):
  print(numbers[i])
  i += 1


