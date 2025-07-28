# Set the correct password
correct_password = "12345"

# Loop until the user guesses the correct password
while True:
    # Ask the user to guess the password
    guess_pswd = input("Enter the password: ")

    # Check if the guess is correct
    if guess_pswd == correct_password:
        print("Congratulations! You've guessed the correct password.")
        break
    else:
        print("Wrong password. Try again.")