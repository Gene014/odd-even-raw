#CALMA, EUGENE MARIE S.
#BSCPE_1-4
# OOP Laboratory Exercise Number 3 Problem 1 (ODD-EVEN-RAW)

##Write a Python program that reads a text file named numbers.txt that contains 20 integers. 
#The program will create two other text file; the first text file will be named even.txt that will contains all even numbers extracted from the numbers.txt. 
#The second text file will be named odd.txt that will contains all odd numbers extracted from the numbers.txt.

#create the ff txt file, must be same path of the current program.
def process():
    # open numbers.txt (read), double txt even.txt (append), triple odd.txt (append)
    with open("numbers.txt","r") as input_file, open("even.txt","w") as even_file, open ("odd.txt","w") as odd_file:
            #read numbers.txt line by line
        for line in input_file:
            input_num = int(line)
                # if int is even
            if input_num % 2 == 0:
                even = input_num
                #write to even txt
                even_file.write(str(even) + "\n")
                # if int is odd
            else:
                odd = input_num
                #write to odd txt
                odd_file.write(str(odd) + "\n")
process()