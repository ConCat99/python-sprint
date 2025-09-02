#Use input() to grab a number value from the user and cast it to a float.
#Divide the new float by any number and cast the result to an int.
#Use input() to grab the name of a user and print "Hello [name]!".

ans = float(input("Enter a number: "))
print(ans)

ans_2 = int(ans/2)
print(ans_2)

username=input("Enter your username: ")
print('Hello',username)

#Grab a number value height from the user and store it as an int.
#Grab a number value width from the user and store it as an int.
#Print the area of a rectangle using the provided height and width.

height=int(input("Enter rectangle height: "))
width=int(input("Enter rectangle width: "))
area=width*height

print(area, 'm2')