secret_number=44
guess=int(input("Guess the number:"))

if(guess>secret_number):
    print("Too High")

elif(guess<secret_number):
    print("Too Low")

else:
    print("Correct!")
