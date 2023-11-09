# Tip calculator
print("Welcome to tip calculator")
bill = input("Enter the total amount of the bill: $")
disc = input("Enter the " + "%" + " for the tip: ")
flt_bill = float(bill)
flt_disc = float(disc)
total_disc = flt_bill*flt_disc/100
total_bill = flt_bill-float(total_disc)
print("The amout to pay is: $" + str(total_bill))