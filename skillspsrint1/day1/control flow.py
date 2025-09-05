# user_grade =int(input("Enter your exam score: "))
#
# if user_grade >= 90 and user_grade <=100:
#     print('You have grade A')
# elif user_grade >= 80 and user_grade <=89:
#     print('You have grade B')
# elif user_grade >= 70 and user_grade <=79:
#     print('You have grade C')
# elif user_grade <=69 and user_grade >=0:
#     print('You have failed')
# else:
#     print('Invalid score')

# user_number=int(input("think of a number between 10 and 20:"))
# if user_number >= 10 and user_number <= 20:
#     print('Good number')
# else:
#     print('Number\'s outside range')
#num= 2

# for num in range (2, 20, 2):
#     print(num)
#
# # use a while loop to countdown from 10 to 1
# while num < =20 and num >=0:
#     print(num)
#
# #ans vv

# count = 10
# while count>=1:
#     print (count)
#     count = count - 1

##--create a guessing game--

##create a random number between 1-10 (secret number)
# from numpy import  random
# secret_num = random.randint( 1, 10)
# # print(secret_num)
# user_guess = None
# while user_guess!=secret_num:
#     user_guess = int(input("Enter your guess: "))
# ##take the user guess input and compare to the secret number (random number)
#     if  user_guess >secret_num:
#         print("Too High")
#     elif user_guess <secret_num:
#         print("Too Low")
#     else :
#         print("Correct number!")


## --dictionaries--

# Create an LIST of customer in a dictionaries - Empty when initialised

# prnt out instructions, enter customer details and type exit to quit

# when loop starts will always be True
# Loop based on user input
# if user types exit, stop the loop
# Store the inputs as first_name, last_name
# add the user inputs into the dictionary

# Print the LIST of dictionaries when the user exits
# set dictionaries by using {}, always key value pairs

customer_dictionary={}

exited= False

while not exited:
    first_name=input("Enter your first name:")
    last_name=input("Enter your last name:")
    customer_dictionary['first_name']=first_name
    customer_dictionary['last_name']=last_name
    print(customer_dictionary)
    if exited:
        print("Thank you for using this program")
    else:
        print(input('would you like to exit?'))
        answer = input('would you like to exit?')
        if answer == 'yes':
            break
        else:
            print("Thank you for using this program")
            exited=False







#EXTENSTION
# search or filter customers by first or last name
# create a second input for name to search for
# find matching customers
# display the results or print no customers found