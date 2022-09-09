import csv

infile = open('steps.csv','r')
outfile = open("avg_steps.csv",'w')
csvfile = csv.reader(infile, delimiter=',')
next(csvfile)

counter1 = 0
counter2 = 0
counter3 = 0
counter4 = 0
counter5 = 0
counter6 = 0
counter7 = 0
counter8 = 0
counter9 = 0
counter10 = 0
counter11 = 0
counter12 = 0

outfile.write("Month, Steps\n")

for record in csvfile:
    if int(record[0]) == 1:
        step1 = int(record[1])
        counter1 += step1
        avg_steps1 = counter1/31
    elif int(record[0]) == 2:
        step2 = int(record[1])
        counter2 += step2
        avg_steps2 = counter2/28
    elif int(record[0]) == 3:
        step3 = int(record[1])
        counter3 += step3
        avg_steps3 = counter3/31
    elif int(record[0]) == 4:
        step4 = int(record[1])
        counter4 += step4
        avg_steps4 = counter4/30
    elif int(record[0]) == 5:
        step5 = int(record[1])
        counter5 += step5
        avg_steps5 = counter5/31
    elif int(record[0]) == 6:
        step6 = int(record[1])
        counter6 += step6
        avg_steps6 = counter6/30
    elif int(record[0]) == 7:
        step7 = int(record[1])
        counter7 += step7
        avg_steps7 = counter7/31
    elif int(record[0]) == 8:
        step8 = int(record[1])
        counter8 += step8
        avg_steps8 = counter8/31
    elif int(record[0]) == 9:
        step9 = int(record[1])
        counter9 += step9
        avg_steps9 = counter9/30
    elif int(record[0]) == 10:
        step10 = int(record[1])
        counter10 += step10
        avg_steps10 = counter10/31
    elif int(record[0]) == 11:
        step11 = int(record[1])
        counter11 += step11
        avg_steps11 = counter11/30
    elif int(record[0]) == 12:
        step12 = int(record[1])
        counter12 += step12
        avg_steps12 = counter12/31
        

csvwriter = csv.writer(outfile)

csvwriter.writerow(["January", avg_steps1]) 
csvwriter.writerow(["February", avg_steps2]) 
csvwriter.writerow(["March", avg_steps3]) 
csvwriter.writerow(["April", avg_steps4]) 
csvwriter.writerow(["May", avg_steps5]) 
csvwriter.writerow(["June", avg_steps6]) 
csvwriter.writerow(["July", avg_steps7]) 
csvwriter.writerow(["August", avg_steps8]) 
csvwriter.writerow(["September", avg_steps9]) 
csvwriter.writerow(["October", avg_steps10]) 
csvwriter.writerow(["November", avg_steps11]) 
csvwriter.writerow(["December", avg_steps12]) 


outfile.close()
