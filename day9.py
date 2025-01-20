age = input("Enter your age: ")
if int(age) >= 17:
    print("You are old enough to learn to drive.")
else:
    print("You must wait", 17 - int(age), "more years before you can learn to drive.")

age = int(input("Enter your age: "))
my_age = 22
if age > my_age:
    if age - my_age == 1:
        print("You are 1 year older than me")
    else:
        print("You are", age - my_age, "years older than me")
elif age == my_age:
    print("We are the same age")
else:
    if my_age - age == 1:
        print("You are 1 year younger than me")
    else:
        print("You are", my_age - age, "years younger than me")

