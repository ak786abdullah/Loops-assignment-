# using for loop (Print numbers from 1 to 10 using a for loop)
for i in range(1,11):# I write 11 in range  becouse in python counting start from 0
    print(i)
    # out put = 1 to 10 
    # using while loop (Print numbers from 1 to 5 using a while loop)
    i=1
    while i<=5:
         print(i)
    i += 1 
         # output= 1 to 5
# Ask the user for a number and use a while loop to count down to 1.
i=1
while i<=input():
     print(i)
     i+=1
    # Print a mini multiplication table for numbers 1 to 3 :(nested loop)
for i in range(1,3):
     for j in range (1,3):
          print(f"{i}x{j}={i*j}")
#Use a loop to print numbers from 0 to 10.
# Stop the loop when the number reaches 6 using break.
for i in range(0,11):
     if i ==6:
         break
print(i)
# Use a loop to print numbers from 0 to 5, but skip number 3 using continue 
for i in range(0,6):
     if i==3:
          print(i)
# Bonus Task: Count the Letters!
#● Ask the user to enter a word.
# ● Use a for loop to print each letter on a new line.
for i in (input()):
    print(i)
