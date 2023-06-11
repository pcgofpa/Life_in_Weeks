#Create a program using math and f-Strings that tells us how many days, weeks, months we have left
#if we were to live until 90 years old.
age = input("What is your current age? ")

#Convert age from years to weeks
time_left = 90 - int(age)
x = time_left * 365
y = time_left * 52
z = time_left * 12

print_message = f"You have {x} days, {y} weeks, {z} months left, or {time_left} years."
print(print_message)