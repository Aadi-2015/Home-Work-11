# Infinite Loop
i = 1
while i in range(1,6):
    print(i)
    print(i)
    print(i)
    print("(STOP)")
    break
n = "Hello"
while n  == "Hello":
    print(n)
    print(n)
    print(n)
    print("(STOP)")
    break
# While Loop
balance = 100
print(f"Your balance is ₹{balance}.")
sp = (int(input("Enter how many rupees you want to spend: ")))
print("Current balance:" , balance - sp)
while balance == 0:
    print("No money Left")
    break
if sp <100:
        print("Not enough money")