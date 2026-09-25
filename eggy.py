dozen_price = 36.00
loose_price = 4.75
dozen = 12


print("     Welcome to Dizon Farm")
print("---------------------------------")
num_of_eggs = int(input("Enter the number of eggs: "))
print("---------------------------------")

print(f"You ordered {num_of_eggs} eggs")

num_of_dozen = num_of_eggs//dozen
loose_egg = num_of_eggs % dozen

print(f"No. of dozen: {num_of_dozen}  at Php 36.00 per dozen")
print(f"No. of loose eggs: {loose_egg} at Php 4.75 each")

total_amount = (loose_egg * loose_price ) + (num_of_dozen * dozen_price)

print(f"Your total amount due is {total_amount}")