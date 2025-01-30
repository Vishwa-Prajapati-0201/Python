"""Write a program that asks the user to enter a length in feet. The program should then give
the user the option to convert from feet into inches, yards, miles, millimeters, centimeters,
meters, or kilometers. Say if the user enters a 1, then the program converts to inches, if they
enter a 2, then the program converts to yards, etc. While this can be done with if statements,
it is much shorter with lists and it is also easier to add new conversions if you use lists."""

units = ["inches", "yards", "miles", "millimeters", "centimeters", "meters", "kilometers"]
conversion_factor = [12, 1/3, 1/5280, 304.8, 30.48, 0.3048, 0.0003048]

feet = float(input("Enter the length in feet: "))

print("\nConvert length into:")
for i in range(len(units)):
    print(f"{i + 1}. {units[i]}")

choice = int(input("\nEnter Your Choice: ")) - 1

length = feet * conversion_factor[choice]
print("\n",feet, "feet =", length, units[choice])