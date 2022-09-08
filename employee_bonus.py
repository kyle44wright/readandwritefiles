import csv

infile = open('EmployeePay.csv','r')

csvfile = csv.reader(infile, delimiter=',')

next(csvfile)

for record in csvfile:
    base_pay = float(record[3])
    bonusv = 1 + float(record[4])
    bonus = base_pay * float(record[4])
    bonus1 = float(bonus)
    bonus2 = "$" + "{:,.2f}".format(bonus1)
    employee_pay = base_pay * bonusv
    clean_pay = "$" + "{:,.2f}".format(employee_pay)
    name = record[1] + ' ' + record[2]
    base_pay_format = "$" + "{:,.2f}".format(base_pay)
    print("Full Name: " + name)
    print("Base Salary: " + base_pay_format)
    print("Bonus: " + bonus2)
    print("Total Pay: " + clean_pay)
    input()





