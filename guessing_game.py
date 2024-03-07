import random
no_by_computer = random.randint(1,100)
attempts = 0
max_attempts = 10

while attempts < max_attempts:
    guess_the_no = int(input("Guess the number: "))
    attempts = attempts + 1

    if guess_the_no < no_by_computer:
        print("The number you guessed is smaller, guess a larger number.")
    elif guess_the_no > no_by_computer:
        print("The number you guessed is bigger, guess a smaller number.")
    else:
        print(f"Congratulations! You guessed the number {no_by_computer} correctly in {attempts} attempts.")
        break
else:
    print(f"are pagal saare chance gwa diye. sahi no to ye {no_by_computer} tha bete. phirse try kr.")

