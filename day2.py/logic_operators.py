age =int(input("Enter the age :"))
has_id =bool(input("Show the ID:"))

if(age>=20 and has_id):
    print("Allowed")
elif(age<13 or age>60):
    print("Discount")
elif(not has_id):
    print("No ID")       