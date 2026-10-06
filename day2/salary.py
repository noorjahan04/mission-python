salary=float(input("Enter your salary:"))
if (salary<30000):
    tax_rate=5
elif (salary<=70000):
    tax_rate=15
else:
    tax_rate=25

print ("final tax rate:", tax_rate,"%")
