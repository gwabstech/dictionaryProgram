from email.policy import default
from tkinter import constants


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

current = True

if current:
    current = False
    print('Turning light off')
elif not current:
    current = True
    print('Turning ligth on')
else:
    print('problem')

loyalty_customer = True
total_bill = 124

if loyalty_customer and total_bill > 100:
    #give 20% discount
    total_bill = total_bill - (float(total_bill) / 100) * 20
elif total_bill > 100:
    #give 10% discount
    total_bill = total_bill - (float(total_bill) / 100) * 10
else:
    #sorry no discount, 5% service charge applied.
    print('Sorry, no discount ...')

print('Total Bill: ', float(total_bill))

http_status_code = 501

match http_status_code:
    case 200:
        print("success")
    case 400:
        print("Bad Request")
    case 404:
        print("Not found")
    case 500 | 501:
        print("Server error")
    case _:
        print("Unknown error")
