import random
import os

"""
This program is designed to improve your vocabulary.
It prompts you to enter your grade level and gives you words to define based on what you input.
It also gives you points based on the difficulty of the question.
"""

#This function is an intro function that tells the user about the program.
easy_wordbank = {'Dearly loved' : 'Beloved', 'Be fully aware of; realize fully' : 'Appreciate', 'Pleasing or delighting' : 'Charming', 'An important, honorable person' : 'Worthy' , 'Providing assistance or serving a useful function' : 'Helpful', 'The ultimate agency predetermining the course of events' : 'Fate'}
medium_wordbank = {'Characteristic of an enemy or one eager to fight' : 'Aggressive', 'Someone who organizes a business venture' : 'Entrepreneur', 'Seeming to come from the time yet to come' : 'Futuristic', 'The state or quality of being recognized' : 'Acknowledgement', 'Expect, believe, or suppose' : 'Imagine', 'Distinctly dissimilar or unlike' : 'Diverse'}
hard_wordbank = {'Sleep inducing' : 'Hypnagogic', 'A state or condition markedly different from the norm' : 'Aberration', 'Agree or express agreement' : 'Acquiesce', 'Liveliness and eagerness' : 'Alacrity', 'Diffusing warmth and friendliness' : 'Amiable', 'Make peace with' : 'Appease'}
all_wordbank = {}
all_wordbank.update(easy_wordbank)
all_wordbank.update(medium_wordbank)
all_wordbank.update(hard_wordbank)
easy_defs = easy_wordbank.keys()
easy_defs_random = random.sample(easy_defs, len(easy_defs))
medium_defs = medium_wordbank.keys()
medium_defs_random = random.sample(medium_defs, len(medium_defs))
hard_defs = hard_wordbank.keys()
hard_defs_random = random.sample(hard_defs, len(hard_defs))
all_defs = all_wordbank.keys()
all_defs_random = random.sample(all_defs, len(all_defs))


def play():
	difficulty = raw_input('Enter Level of difficulty; "Easy", "Medium", "Hard", "All": ')
	if difficulty == "Easy":
		play_easy()
	elif difficulty == "Medium":
		play_medium()
	elif difficulty == "Hard":
		play_hard()
	elif difficulty == "All":
		play_all()
	else:
		"Invalid Input!"
		play()

	

def play_easy():
	points = 0
	num = 1
	num_right = 0
	for key,val in easy_wordbank.items():
			print key, ":", val
			print ""
	raw_input("Press enter to continue...")
	os.system("clear")
	for a in easy_wordbank:
		print easy_wordbank[a],
	print ""
	for a in easy_defs_random:
		ans = raw_input("""Question %d: %s 
			Answer: """ % (num, a))
		num += 1
		if ans == easy_wordbank[a]:
			points += 5
			num_right += 1
			print ("You're correct. You won 5 points! %d/%d questions right." % (num_right, (len(easy_defs))))
			print ""
		else:
			print("You were wrong, the correct answer is %s. %d/%d questions right." %(easy_wordbank[a], num_right, (len(easy_defs))))
			print ""
	if num_right == len(easy_defs):
		print("Congratulations! You got all the questions right and acquired %d points" % (points))
	else:
		print("You answered %d/%d questions correctly and you acquired %d points" % (num_right, (len(easy_defs)), points))
	raw_input("Press enter to continue...")
	os.system("clear")

def play_medium():
	points = 0
	num = 1
	num_right = 0
	for key,val in medium_wordbank.items():
			print key, ":", val
			print ""
	raw_input("Press enter to continue...")
	os.system("clear")
	for a in medium_wordbank:
		print medium_wordbank[a],
	print ""
	for a in medium_defs_random:
		ans = raw_input("""Question %d: %s 
			Answer: """ % (num, a))
		num += 1
		if ans == medium_wordbank[a]:
			points += 10
			num_right += 1
			print ("You're correct. You won 10 points! %d/%d questions right." % (num_right, (len(medium_defs))))
			print ""
		else:
			print("You were wrong, the correct answer is %s. %d/%d questions right." %(medium_wordbank[a], num_right, (len(medium_defs))))
			print ""
	if num_right == len(medium_defs):
		print("Congratulations! You got all the questions right and acquired %d points" % (points))
	else:
		print("You answered %d/%d questions correctly and you acquired %d points" % (num_right, (len(medium_defs)), points))
	raw_input("Press enter to continue...")
	os.system("clear")

def play_hard():
	points = 0
	num = 1
	num_right = 0
	for key,val in all_wordbank.items():
			print key, ":", val
			print ""
	raw_input("Press enter to continue...")
	os.system("clear")
	for a in hard_wordbank:
		print hard_wordbank[a],
	print""
	for a in hard_wordbank:
		ans = raw_input("""Question %d: %s 
			Answer: """ % (num, a))
		num += 1
		if ans == hard_wordbank[a]:
			points += 20
			num_right += 1
			print ("You're correct. You won 20 points! %d/%d questions right." % (num_right, (len(hard_defs))))
			print ""
		else:
			print("You were wrong, the correct answer is %s. %d/%d questions right." %(all_wordbank[a], num_right, (len(hard_defs))))
			print ""
	if num_right == len(hard_defs):
		print("Congratulations! You got all the questions right and acquired %d points" % (points))
	else:
		print("You answered %d/%d questions correctly and you acquired %d points" % (num_right, (len(hard_defs)), points))
	raw_input("Press enter to continue...")
	os.system("clear")

def play_all():
	points = 0
	num = 1
	num_right = 0
	for key,val in all_wordbank.items():
			print key, ":", val
			print ""
	raw_input("Press enter to continue...")
	os.system("clear")
	for a in all_wordbank:
		print all_wordbank[a],
	print ""
	for a in all_defs_random:
		ans = raw_input("""Question %d: %s 
			Answer: """ % (num, a))
		num += 1
		if ans == all_wordbank[a]:
			num_right += 1
			if a in easy_defs:
				points += 5
				print ("You're correct. You won 5 points! %d/%d questions right." % (num_right, (len(all_defs))))
			elif a in medium_defs:
				points += 10
				print("You're correct. You won 10 points! %d/%d questions right." % (num_right, (len(all_defs))))
			else:
				points += 20
				print("You're correct. You won 20 points! %d/%d questions right." % (num_right, (len(all_defs))))
			print ""
		else:
			print("You were wrong, the correct answer is %s. %d/%d questions right." %(all_wordbank[a], num_right, (len(all_defs))))
			print ""
	if num_right == len(all_defs):
		print("Congratulations! You got all the questions right and acquired %d points" % (points))
	else:
		print("You answered %d/%d questions correctly and you acquired %d points" % (num_right, (len(all_defs)), points))
	raw_input("Press enter to continue...")
	os.system("clear")



def word_bank():
	bank_choice = raw_input('What Word Bank do you want to see ("Easy", "Medium", "Hard", "All"): ')
	print ""
	if bank_choice == "Easy":
		for key,val in easy_wordbank.items():
			print key, ":", val
			print ""
	elif bank_choice == "Medium":
		for key,val in medium_wordbank.items():
			print key, ":", val
			print ""
	elif bank_choice == "Hard":
		for key,val in hard_wordbank.items():
			print key, ":", val
			print ""
	elif bank_choice == "All":
		for key,val in all_wordbank.items():
			print key, ":", val
			print ""
	else:
		print "Invalid Input!"
		word_bank()
	raw_input("Press enter to continue...")



def generate_question(question_num, question_def):
	question = raw_input("Question %d: %s" % (question_num, question_def))


def info():
	print "You will be given the definition of a word and you'll be asked to give one word that corresponds with that definition. When you're done, you're told how many questions you got right and how many points you acquired. Have Fun! "
	raw_input("Press enter to continue...")



