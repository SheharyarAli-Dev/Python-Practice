print("Hello World"); #Prints Simple Statement on new line

print("Hello ","World", sep="-"); #using sep we can add anything in middle where commas are placed between strings

print("Hello World",end="2nd Line"); # Using end we can add anything in end, this will cause the control to stay on current line rather than using new line when another print statement is used

print("Check");

age=5;

#f strings are used to print variable value inside strings using {}

print(f"My age is {age}");

age=input("Enter your age: "); #gets input and always returns a string
print(f"Your age is {age}");

#to convert it to number say float

age=float(input("Age: "));
print(f"Your age is {age}");

