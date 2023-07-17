
# miles = input("Enter Miles ")
# miles = int(miles)
# kilometers = miles * 1.60934
# print("{} miles = {} kilometers".format(miles, kilometers))

age = eval(input("Enter age: "))
if age < 5:
    print("Too young for school")
elif age == 5:
    print("Go to Kindergaten")
elif (age > 5) and (age <= 17):
    grade = age - 5
    print("Go to grade {}".format(grade))
else:
    print("Go to college")