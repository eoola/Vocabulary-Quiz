from Vocabulary_Quiz import *
import os
import sys

def welcome():
	os.system('clear')
	user_choice = raw_input('''Welcome to Demi's Vocabulatron Game.
		Inputs are case-sensitive
		Type "Word Bank" to view the words and their meaning
		Type "Play" to play the game
		Type "Info" for more information about the game
		Type "Quit" to end the program
		Enter "Word Bank", "Play", "Info", or "Quit":  ''') #Gives the user options to start the game, request info, request the word bank, or quit the game.
	if user_choice == "Word Bank":
		os.system('clear')
		word_bank()
		welcome()
	elif user_choice == "Info":
		os.system('clear')
		info()
		welcome()
	elif user_choice == "Play":
		os.system('clear')
		play()
		welcome()
	elif user_choice == "Quit":
		os.system('clear')
		sys.exit(0)
	else:
		os.system('clear')
		print "Invalid input"
		welcome()

welcome()
