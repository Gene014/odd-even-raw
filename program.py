#CALMA, EUGENE MARIE S.
#BSCPE_1-4
# OOP Laboratory Exercise Number 3 Problem 1 (ODD-EVEN-RAW)

##Write a Python program that reads a text file named numbers.txt that contains 20 integers. 
#The program will create two other text file; the first text file will be named even.txt that will contains all even numbers extracted from the numbers.txt. 
#The second text file will be named odd.txt that will contains all odd numbers extracted from the numbers.txt.

#greetings

#create the ff txt file, must be same path of the current program.
def process():
    # input and inserting your acount name
    account_name = input("\n\33[33mHi, Good day! Please enter your name.\33[0m ")
# data protection policy
    while True:
        user_input = input("\n\33[1m In compliance with the Data Privacy Act of 2012 and its Implementing Rules and Regulations, we execute reasonable and appropriate security measures for the protection of personal data that we collect. Please type \33[32mYes\33[0m\33[1m if you want to continue, otherwise, type \033[31mNo\033[0m\33[1m if you want to terminate this process.\33[0m ")
        if user_input.lower() == 'yes':
            print("Please wait... Generating your data.")
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
        elif user_input.lower() == 'no':
            print("\33[41mTerminating Program...\33[41m ")
            exit()
        else:
            print('Type yes/no')
process()