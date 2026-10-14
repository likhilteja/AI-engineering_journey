#print the multiplication table of any number (1 to 10).

num = int(input("Enter the multiplication table number : "))
for i in range (1,11):
     print(f"{num}*{i} = {num*i}")