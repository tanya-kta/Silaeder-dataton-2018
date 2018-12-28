data = {"Moscow":(1, 2, 100, 0)} # city:(lan, log, population, used)

user_stat = 0
comp_stat = 0
def find_city_in_data(city):
	if(city in data):
		return True
	return False

def return_statistic():
	if user_stat > comp_stat:
		return {"player":user_stat, "computer":comp_stat, "winner":"player"}
	elif user_stat == comp_stat:
		return {"player":user_stat, "computer":comp_stat, "winner":"draw"}
	else:
		return {"player":user_stat, "computer":comp_stat, "winner":"computer"}

def information_city(city):
	if find_sity_in_data(city):
		return {"coordinates":(data[city][0], data[city][1]), "population": data[city][2], "used":data[city][3]}
	return {city: None}

def low(word):
	if word is None:
		return word
	else
		return word.lower()

def get_reply(prev_city, city):
	prev_city = low(prev_city)
	city = low(city)
	if !find_city_in_data(city):
		return {"ok":False, "error":"not in data"}
	if !(prev_city is None) and (prev_city[-1] != city[0]):
		return {"ok":False, "error":"mistake"}
	

if __name__ == "__main__":
	print()