import csv 

infile = open('customers.csv','r')
outfile = open("customer_country.csv",'w')

csvfile = csv.reader(infile, delimiter=',')

next(csvfile)

outfile.write("Full Name, Country\n")

for record in csvfile:
    name = record[1] + ' ' + record[2]
    country = record[4]

    outfile.write(name + ',' + country + '\n')

outfile.close()

        


