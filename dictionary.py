'''staff = {"Name":"Vijay","Age":33,"Salary":41000,"Company":"jio"}

# print(type(staff))
#
# print("Show staff data...")
# print(staff)

for i in staff.items():     # it prints the keys and items both
        print(i)

for i in staff.values():    # staff.keys() is only prints keys
    print(i)

for i in staff.keys():      # staff.values() it prints only values
      print(i)'''

#staff = {"Name":"Vijay","Age":33,"Salary":41000,"Company":"jio"}
# print(type(staff))
# print("Show staff data...")
# print(staff)
#
# print("deleting some of the staff data")
# del staff["Name"]
# del staff["Company"]
#
# print("printing the modified information")
# print(staff)
# print("Deleting the dictionary: staff");
# del staff
# print("lets try to print it again")
# print(staff)


# staff={"Name":"Vijay","Age":33,"Salary":30000,"Company":"jio"}
#
# print(type(staff))
# print("First print the existing dictionary...")
# print(staff)
#
# print("Lets update the staff dictionary")
#
# print("Enter the staff details: ")
#
# staff["Name"] = input("Name: ");
# staff["Age"] = int(input("Age: "));
# staff["Salary"] = int(input("Salary: "));
# staff["Company"] = input("Company: ");
#
# print("Printing the new updated data")
# print(staff)


staff={"Name":"vijay","Age":24,"Salary":30000,"Company":"openai"}

print(type(staff))

print("show the staff data...")
print("Name : %s" %staff["Name"])
print("Age : %d" %staff["Age"])
print("Salary : %d" %staff["Salary"])
print("Company : %s" %staff["Company"])





