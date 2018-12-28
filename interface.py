#from backend import some_function as get_reply
#from backend import some_function as get_city_info


def start():
	""" First function to be executed,
Says hello to user """
	print("Hello! That's the KaKoSi's application licensed by Muffinware License")
	print("If you want to LET UP, type symbol - and we will finish the game")
	print("Let's start a game!\n")

def game():
	""" Main function that supports
communication with player """
	last_city = None
	while True:
		city = input("Enter a city: ")
		reply = get_reply(last_city, city)
		if not reply['ok']:
			if(reply['error'] == "used"):
				print("We've already used this city", end='')
			elif(reply['error'] == "letter"):
				print("You have to enter a city that starts with letter {}".format(last_city[-1].upper()), end='')
			else:
				print("You've entered a city I don't know", end='')
			print("... Try again, please")
			continue
		info = get_city_info(city)
		print("You've entered a city with coordinates {} with population {}".format(*info)) # Instead of this there'll be a plot drawing
		info = get_city_info(reply['city'])
		print("I chosed a city with coordinates {} with population {}".format(*info))
		last_city = reply['city']

if __name__ == "__main__":
	start()
	game()
	exit(0)