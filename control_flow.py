bill_total = 90

discount1 = 10
discount2 = 20

if bill_total > 100:
    print("Bill is greater than 100!")
    bill_total = bill_total -discount1
else:
    print("Bill is less than 100!")
    bill_total = bill_total - discount2

print("Total bill "+ str(bill_total))