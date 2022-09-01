def main():
    infile=open('clients.txt','r')
    i = 0

    for line in infile:
        line = line.rstrip('\n')
        i += 1
        print(str(i) + '.' + ' ' + line)


main()

#Alternate solution

#infile = open('clients.txt','r')

#counter = 1

#for line in infile:
    #print(counter,". ", line.rstrip('\n'),sep='')

    #counter += 1 

