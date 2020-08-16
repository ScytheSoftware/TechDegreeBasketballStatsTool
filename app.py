#DaVonte' Whitfield
#Python 3.7
#Tech Degree Project 2 Basketball Stats Tool
#I mainly used methods I did on the first project

import constants
import os
import re
import pdb
import copy

def clear():  #Note, This works with python program about not in Visual Studios, at least for me.
	os.system("cls" if os.name == "nt" else "clear")
#nt is a window check, if you are on window use cls, else clear(Mac)


def clean_data(data):
	#the guardian cleaning is not in this function. it's inside the display function(s)

	num=0
	#This is for height
	for index in data:

		temp_height = (index['height']).split(' ')

		temp_height = int(temp_height[0]) #zero is here because the number is always in the zero poistion

		(data[num])['height'] = temp_height

		#This is for experience
		if (index['experience']) == 'YES':
			(data[num])['experience'] = True

		else:
			(data[num])['experience'] = False

		if 'and' in index['guardians']: #This is to drop the and in guardians
			(data[num])['guardians'] = re.sub(r'( and)',',',index['guardians'])

		num += 1

def stats_tool_title():

	header = "basketball team stats tool"
	menu = "Menu"

	print("*" * len(header), '\n')
	print(header.title(), '\n')
	print("*" * len(header))
	print("-" * len(menu), menu.upper(),"-" * len(menu))
	print("")


def refresh():
	clear()
	stats_tool_title()


def display_panthers(team_roster):

	header = "|Team: Panthers Stats"
	name_list = []
	guardian_list = []
	experience_count = 0
	inexperience_count = 0
	avg_height = 0
	number_of_players = 0

	
	for person in team_roster:
		number_of_players += 1

		for info in person:
			#Names
			if info == 'name':
				name_list.append(person[info])

			#Guardians
			elif info == 'guardians':
				guardian_list.append(person[info])

			#Experience
			elif info == 'experience' and person[info] == True:
				experience_count +=1

			elif info == 'experience' and person[info] == False:
				inexperience_count +=1

			#Height
			elif info == 'height':
				avg_height += person[info]

				if number_of_players == len(team_roster):
					avg_height = avg_height / len(team_roster)
	
	print("\n")
	print(header)
	print("-" * len(header), "\n")

	print("|Total Players: {}".format(number_of_players))
	print("|Total Experienced: {}".format(experience_count))
	print("|Total Inexperienced: {}".format(inexperience_count))
	print("|Average Height: {}".format(round(avg_height)))

	print("\n")
	print("|Players on Team:")
	print("----------------")
	print(*name_list, sep = ", ") # line from: https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/

	print("")
	print("|Guardians:")
	print("----------")
	print(*guardian_list, sep = ", ")


def display_bandits(team_roster):
	header = "|Team: Bandits Stats"
	name_list = []
	guardian_list = []
	experience_count = 0
	inexperience_count = 0
	avg_height = 0
	number_of_players = 0

	
	for person in team_roster:
		number_of_players += 1

		for info in person:
			#Names
			if info == 'name':
				name_list.append(person[info])

			#Guardians
			elif info == 'guardians':
				guardian_list.append(person[info])

			#Experience
			elif info == 'experience' and person[info] == True:
				experience_count +=1

			elif info == 'experience' and person[info] == False:
				inexperience_count +=1

			#Height
			elif info == 'height':
				avg_height += person[info]

				if number_of_players == len(team_roster):
					avg_height = avg_height / len(team_roster)
	
	print("\n")
	print(header)
	print("-" * len(header), "\n")

	print("|Total Players: {}".format(number_of_players))
	print("|Total Experienced: {}".format(experience_count))
	print("|Total Inexperienced: {}".format(inexperience_count))
	print("|Average Height: {}".format(round(avg_height)))

	print("\n")
	print("|Players on Team:")
	print("----------------")
	print(*name_list, sep = ", ") # line from: https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/

	print("")
	print("|Guardians:")
	print("----------")
	print(*guardian_list, sep = ", ")


def display_warriors(team_roster):

	header = "|Team: Warriors Stats"
	name_list = []
	guardian_list = []
	experience_count = 0
	inexperience_count = 0
	avg_height = 0
	number_of_players = 0

	
	for person in team_roster:
		number_of_players += 1

		for info in person:
			#Names
			if info == 'name':
				name_list.append(person[info])

			#Guardians
			elif info == 'guardians':
				guardian_list.append(person[info])

			#Experience
			elif info == 'experience' and person[info] == True:
				experience_count +=1

			elif info == 'experience' and person[info] == False:
				inexperience_count +=1

			#Height
			elif info == 'height':
				avg_height += person[info]

				if number_of_players == len(team_roster):
					avg_height = avg_height / len(team_roster)
	
	print("\n")
	print(header)
	print("-" * len(header), "\n")

	print("|Total Players: {}".format(number_of_players))
	print("|Total Experienced: {}".format(experience_count))
	print("|Total Inexperienced: {}".format(inexperience_count))
	print("|Average Height: {}".format(round(avg_height)))

	print("\n")
	print("|Players on Team:")
	print("----------------")
	print(*name_list, sep = ", ") # line from: https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/

	print("")
	print("|Guardians:")
	print("----------")
	print(*guardian_list, sep = ", ")


if __name__ == '__main__':
	#Full Balanced Teams
	panthers_team =[]
	bandits_team=[]
	warriors_team=[]

	#To make the teams balance
	panthers_experience_list =[]
	Bandits_experience_list =[]
	Warriors_experience_list =[]
	exp_placement = False #exp is experience

	tool_on =True
	fixed = False #For input handling

	#Deep Copy All of the info
	new_player = copy.deepcopy(constants.PLAYERS)

	for items in range(len(new_player)):

		data_placeholder = new_player[items]
		exp_placement = False

		if data_placeholder['experience'] == 'YES': #Because the data is uppercase, I used cap

			#For the experience
			while exp_placement != True:
				if panthers_experience_list.count('YES') < 3:
					panthers_experience_list.append('YES')
					panthers_team.append(data_placeholder)
					exp_placement = True

				elif Bandits_experience_list.count('YES')< 3:
					Bandits_experience_list.append('YES')
					bandits_team.append(data_placeholder)
					exp_placement = True

				elif Warriors_experience_list.count('YES')<3:
					Warriors_experience_list.append('YES')
					warriors_team.append(data_placeholder)
					exp_placement = True
		else:
			#For the inexperience
			while exp_placement != True:
				if panthers_experience_list.count('NO') < 3:
					panthers_experience_list.append('NO')
					panthers_team.append(data_placeholder)
					exp_placement = True

				elif Bandits_experience_list.count('NO')< 3:
					Bandits_experience_list.append('NO')
					bandits_team.append(data_placeholder)
					exp_placement = True

				elif Warriors_experience_list.count('NO')<3:
					Warriors_experience_list.append('NO')
					warriors_team.append(data_placeholder)
					exp_placement = True


	#Cleaning each Team
	clean_data(panthers_team)
	clean_data(bandits_team)
	clean_data(warriors_team)


	while tool_on == True:

		refresh()
		print("Display your favorite team's stats! Here are your choices:")
		print("Press [1] to Display Team Stats")
		print("Press [2] to Quit")
		choice = input(">> ")

		fixed = False #Resetting fixed

		while fixed != True:
			if choice == '1' or choice == '2':
				fixed = True

			else:
				print("Invaild entry. The options are [1] or [2]. Try again.")
				choice = input(">> ")

		if choice == "1":
			refresh()
			for options in range(len(constants.TEAMS)): 
				print("Press [{}] for {}".format(options + 1, constants.TEAMS[options]))

			team_selection = input(">> ")

			fixed = False #Resetting fixed

			while fixed != True:
				if team_selection == '1' or team_selection == '2' or team_selection == '3':
					fixed = True

				else:
					print("Invaild entry. The options are [1], [2], or [3]. Try again.")
					team_selection = input(">> ")

			refresh()

			if team_selection == "1":
				display_panthers(panthers_team)

			elif team_selection == "2":
				display_bandits(bandits_team)

			elif team_selection == "3":
				display_warriors(warriors_team)
		
			print("\n")
			print("Press [1] to reset to stat tool")
			print("Press [2] to Quit")
			try_again = input(">> ")

			fixed = False #Resetting fixed

			while fixed != True:
				if try_again == "1" or try_again == "2":
					fixed = True

				else:
					print("Invaild entry. The options are [1] or [2]. Try again")
					try_again = input(">> ")

			if try_again == "1":
				continue

			elif try_again == "2":
				tool_on = False
				confirm_choice = (input("Are you sure you want to exit? [y]es/[n]o \n>> ")).lower()

				fixed = False #Resetting fixed

				while fixed != True:
					if confirm_choice == "y" or confirm_choice == "n":
						fixed = True

					else:
						print("Invaild entry. The options are [y] or [n]. Try again")
						confirm_choice = (input(">> ")).lower()

				if confirm_choice == 'n':
					tool_on = True

		elif choice == "2":
			tool_on = False
			confirm_choice = (input("Are you sure you want to exit? [y]es/[n]o \n>> ")).lower()

			fixed = False #Resetting it

			while fixed != True:
				if confirm_choice == "y" or confirm_choice == "n":
					fixed = True

				else:
					print("Invaild entry. The options are [y] or [n]. Try again")
					confirm_choice = (input(">> ")).lower()

			if confirm_choice == 'n':
				tool_on = True
