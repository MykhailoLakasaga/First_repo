#print ("Hello World")

#print ("Hello Git")

#name = 'Wendy\'s dog'
#print(name)

#name = input("What's your name? ")
#print("Hello! " + name + " How are you?")

# Змініть вхідні дані на ціле число
#age = int(input('How old are you now?'))
#print('How old will you be next year?')
#print(age + 1)


my_lucky_number = 7
guess = int(input("Guess my lucky number! I think it is: "))
while my_lucky_number != guess:
     guess = int(input("Oops! Not it. Try again: "))
print("Congrats! You guessed it.")
