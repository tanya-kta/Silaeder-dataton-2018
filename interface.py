import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from backend import get_reply
from backend import get_city_information as get_city_info
from backend import get_statistic as get_stats


def start():
	""" First function to be executed,
Says hello to user """
	print("Hello! That's the KaKoSi's application licensed by Muffinware License")
	print("If you want to LET UP, type symbol - and we will finish the game")
	print("Let's start a game!\n")

def draw_plot(city_lat, city_lon, city_name, title=''):
	""" Draws a plot """
	plt.figure(figsize=(16, 16))
	plt.title(title)
	m = Basemap(projection='lcc', resolution=None,
				width=8E6, height=8E6, 
				lat_0=city_lat, lon_0=city_lon)
	m.etopo(scale=0.5, alpha=0.5)
	x, y = m(city_lon, city_lat)
	plt.plot(x, y, 'ok', markersize=5)
	plt.text(x, y, city_name, fontsize=12)
	plt.show()

def game():
	""" Main function that supports
communication with player """
	last_city = None
	while True:
		city = input("Enter a city: ")
		if(city == '-'):
			break
		reply = get_reply(last_city, city)
		if not reply['ok']:
			if(reply['error'] == "is used"):
				print("We've already used this city", end='')
			elif(reply['error'] == "mistake"):
				print("You have to enter a city that starts with letter {}".format(last_city[-1].upper()), end='')
			else:
				print("You've entered a city I don't know", end='')
			print("... Try again, please")
			continue
		info = get_city_info(city)
		draw_plot(info['coordinates'][1], info['coordinates'][0], city, 'Your city')
		#print("You've entered a city with coordinates {} with population {}".format(info['coordinates'], info['population'])) # Instead of this there'll be a plot drawing
		if reply['city'] is None:
			break
		info = get_city_info(reply['city'])
		print("I chose {}".format(reply['city']))
		draw_plot(info['coordinates'][1], info['coordinates'][0], reply['city'], "Computer's city")
		#print("I chosed a city with coordinates {} with population {}".format(info['coordinates'], info['population'])) # Instead of this there'll be a plot drawing
		last_city = reply['city']

def finish():
	print("Game is finished. Results: {}".format(get_stats()))

if __name__ == "__main__":
	start()
	game()
	finish()
	exit(0)