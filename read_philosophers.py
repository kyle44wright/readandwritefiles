def main():
    infile = open('philosophers.txt','r')

    #file_contents = infile.read()

    line1 = infile.readline().rstrip('\n')
    Line2 = infile.readline().rstrip('\n')
    Line3 = infile.readline().rstrip('\n')

    #print(file_contents)

    print(line1)
    print(Line2)
    print(Line3)

main()
