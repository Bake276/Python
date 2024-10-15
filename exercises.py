import random, os

def rock_paper_scissors():
    play_again = "y"

    while play_again == "y":
        player_score = 0
        computer_score = 0

        while player_score < 2 and computer_score < 2:
            player_choice = input("Rock, Paper, Scissors: ").lower()
            computer_choice = random.choice(["rock", "paper", "scissors"])

            if player_choice == "rock":
                if computer_choice == "scissors":
                    player_score += 1
                if computer_choice == "paper":
                    computer_score += 1

            if player_choice == "paper":
                if computer_choice == "rock":
                    player_score += 1
                if computer_choice == "scissors":
                    computer_score += 1

            if player_choice == "scissors":
                if computer_choice == "paper":
                    player_score += 1
                if computer_choice == "rock":
                    computer_score += 1

            print("")
            print(f"The computer chose {computer_choice}")
            print(f"Player: {player_score} - Computer: {computer_score}")
            print("")

        if player_score > computer_score:
            print("You win!!!")
        else:
            print("The Computer wins :(")

        print("")
        play_again = input("Play again (y/n): ").lower()
        print("")


rock_paper_scissors()





def password_generator():
	letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	numbers = "0123456789"
	symbols = "$%!=?-_"

	user_letters = int(input("How many letters: "))
	user_numbers = int(input("How many numbers: "))
	user_symbols = int(input("How many symbols: "))

	password = []

	for _ in range(user_letters):
		password.append(random.choice(letters))

	for _ in range(user_numbers):
		password.append(random.choice(numbers))

	for _ in range(user_symbols):
		password.append(random.choice(symbols))

	random.shuffle(password)
	password = "".join(password)

	return f"Your password is: {password}"


# print(password_generator())







def hangman():
    print("Welcome to Hangman")
    print("You have six tries to guess a word")
    print()

    word = random.choice(["thorsten", "becker", "envelope", "underground", "chess"])
    word_list = list(word)
    word_to_guess = list("_" * len(word))
    lives_total = 6
    lives_left = 6

        
    while lives_left > 0:
        print(f"**********{lives_left}/{lives_total} LIVES LEFT**********")
        print(f"Word to guess: {"".join(word_to_guess)}")
        letter = input("Guess a letter: ").lower()
        print()
        
        if letter in word_to_guess:
            print("You already guessed that")
            print()
            continue

        if letter in word_list:
            while letter in word_list:
                index_letter = word_list.index(letter)
                word_list.pop(index_letter)
                word_list.insert(index_letter, "-")
                word_to_guess.pop(index_letter)
                word_to_guess.insert(index_letter, letter)
        else:
            print(f"You guessed {letter}, that's not in the word.")
            print()
            lives_left -= 1


        if lives_left == 0:
            print(f"You lost the game. The word was {word}")
        
        if "".join(word_to_guess) == word:
            print("".join(word_to_guess))
            print("You won the game!!")
            break

# hangman()







def caesar_cipher():
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	play_again = "yes"


	def encode_decode(message, shift_number, action):
		output_message = ""

		# setzt die shift_number auf -
		if action == "decode":
			shift_number *= -1

		for letter in message:
			if letter.isalpha():
				index = alphabet.index(letter)
				output_message += alphabet[(index + shift_number) % len(alphabet)]
			else:
				output_message += letter
		
		return output_message


	while play_again == "yes":

		action = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
		if action != "encode" and action != "decode":
			print("I don't know what you want!")
			print()
			continue

		message = input("Type your message:\n").lower()
		shift_number = int(input("Type the shift number:\n"))

		output = encode_decode(message, shift_number, action)
		
		print(f"Here's the result: {output}")
		print()

		play_again = input("Type 'yes' if you want to play again. Otherwise type 'no'\n").lower()


# caesar_cipher()







def secret_auction():
	print("Welcome to the secret auction program.")

	other_bidder = "yes"
	bids = {}


	def highest_bidder(bids_dict):
		result = {}
		
		for key, value in bids_dict.items():	
			if not result:
				result[key] = value
				continue

			if value > next(iter(result.values())):
				result = {key: value}

			if value == next(iter(result.values())):
				result[key] = value

		return result



	while other_bidder == "yes":
		name = input("What is your name: ").title()
		if name in bids:
			print("This name is already taken. Choose another one.")
			continue

		bid = int(input("What is your bid: $"))

		bids[name] = bid

		other_bidder = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

		os.system("clear")



	output = highest_bidder(bids)
	
	if len(output) > 1:
		winners = list(output)
		highest_bid = max(output.values())
		print("We have more than one highest bid.")
		print(f"{", ".join(winners[:-1])} and {winners[-1]} bid ${highest_bid} and have to bid again.")
	else:
		winner = next(iter(output.keys()))
		highest_bid = next(iter(output.values()))
		print(f"{winner} won the auction with a bid of ${highest_bid}.")


# secret_auction()







def calculator():
    def add(num1, num2):
        return num1 + num2
    
    def substract(num1, num2):
        return num1 - num2
    
    def multiply(num1, num2):
        return num1 * num2
    
    def divide(num1, num2):
        return num1 / num2
    

    calculate = {
        "+": add,
        "-": substract,
        "*": multiply,
        "/": divide
    }


    continue_calc = "y"
    a = float(input("What's the first number: "))


    while continue_calc == "y":
        operation = input("Pick an operation (+-*/): ")
        b = float(input("What's the next number: "))

        result = calculate[operation](a, b)

        print(f"{a} {operation} {b} = {result}")

        continue_calc = input(f"Type 'y' to continue calculating with {result} or 'n' to start over: ").lower()

        if continue_calc == "y":
            a = result
        elif continue_calc == "n":
            os.system("clear")
            calculator()
        else:
            print("Thank you for using the calculator.")
            return
  
# calculator()


