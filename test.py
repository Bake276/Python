
import random, os
#test for pulling

# def calculator():
#     def add(num1, num2):
#         return num1 + num2
	
#     def substract(num1, num2):
#         return num1 - num2
	
#     def multiply(num1, num2):
#         return num1 * num2
	
#     def divide(num1, num2):
#         return num1 / num2
	
#     continue_calc = "y"
#     a = float(input("What's the first number: "))

#     while continue_calc == "y":
#         operation = input("Pick an operation (+-*/): ")
#         b = float(input("What's the next number: "))

#         if operation == "+":
#             result = add(a, b)
#         elif operation == "-":
#             result = substract(a, b)
#         elif operation == "*":
#             result = multiply(a, b)
#         else:
#             result = divide(a, b)

#         print(f"{a} {operation} {b} = {result}")

#         continue_calc = input(f"Type 'y' to continue calculating with {result} or 'n' to start over: ").lower()

#         if continue_calc == "y":
#             a = result
#         elif continue_calc == "n":
#             os.system("clear")
#             calculator()
#         else:
#             print("Thank you for using the calculator.")
#             return

# calculator()




def blackjack():
	deck_of_cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J" ,"Q", "K", "A"]


	def get_card():
		return random.choice(deck_of_cards)
	

	
	def get_score(hand):
		score = []
		for card in hand:
			if card == "A":
				score.append(11)
			elif card == "J" or card == "Q" or card == "K":
				score.append(10)
			else:
				score.append(card)
		return sum(score)

	

	def evaluate_hand(player, computer, status=True):
		player_score = get_score(player)

		print()
		print(f"Your cards: {player}, current score: {player_score}")
		print(f"Computer's first card: {computer[0]}")
		print()

		if player_score > 20 or status == False:
			win_or_bust(player_score, player, computer)

	

	def win_or_bust(player_final_score, player_final_hand, computer_hand):
		if player_final_score < 21:
			computer_result = computer_plays(computer_hand)
			computer_final_hand = computer_result[0]
			computer_final_score = computer_result[1]
		else:
			computer_final_hand = computer_hand
			computer_final_score = get_score(computer_final_hand)


		print(f"Your final hand: {player_final_hand}, final score: {player_final_score}")
		print(f"Computer's final hand: {computer_final_hand}, final score: {computer_final_score}")
		print()

		if player_final_score == 21:
			print("You have BlackJack! You win!")
		elif player_final_score > 21:
			print("You went over. You lose.")
		elif player_final_score < 21 and player_final_score > computer_final_score:
			print("You win!")
		elif player_final_score < 21 and player_final_score < computer_final_score:
			if computer_final_score == 21:
				print("The Computer has BlackJack. It wins")
			elif computer_final_score > 21:
				print("You win!")                
			else:
				print("The Computer wins.")
		else:
			print("It's a draw.")

		blackjack()
		

	
	def computer_plays(computer_hand):
		computer_hand.append(get_card())
		result = get_score(computer_hand)
		
		while result < 17:
			computer_hand.append(get_card())
			result = get_score(computer_hand)

		return [computer_hand, result]



	print()
	play_game = input("Do you want to play a game of blackjack (y/n): ").lower()

	if play_game == "y":
		os.system("clear")
	else:
		return


	player_hand = [get_card(), get_card()]
	computer_hand = [get_card()]
	evaluate_hand(player_hand, computer_hand)

	print()
	another_card = input("Do you want another card (y/n): ").lower()
	print()

	while another_card == "y":
		player_hand.append(get_card())
		evaluate_hand(player_hand, computer_hand)
		another_card = input("Do you want another card (y/n): ").lower()

	if another_card == "n":
		evaluate_hand(player_hand, computer_hand, False)
		

# blackjack()





def name_shuffler(name):
	return " ".join(name.split(" ")[::-1])

# print(name_shuffler("Thorsten Becker"))



# Test commit
