userinput = input("Enter elements separated by space.")
set1 = set(userinput.split())
userinput1 = input("Enter elements separated by space.")
set2 = set(userinput1.split())
green = set1.intersection(set2)
print(green)