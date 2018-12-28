data = {"Moscow":[1, 2, 100, False], "Omom":[1, 2, 100, False]} # city:(lan, log, population, used)

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
	if find_city_in_data(city):
		return {"coordinates": (data[city][0], data[city][1]), "population": data[city][2], "used": data[city][3]}
	return None

def low(word):
	if word is None:
		return word
	else:
		return word.lower()

def get_reply(prev_city, city):
	prev_city = low(prev_city)
	city = low(city)
	city = city[0].upper() + city[1:]
	if prev_city is not None
	prev_city = prev_city[0].upper() + prev_city[1:]
	if not find_city_in_data(city):
		return {"ok": False, "error": "not in data"}
	if (prev_city is not None) and (low(prev_city[-1]) != low(city[0])):
		return {"ok": False, "error": "mistake"}
	if information_city(city)["used"]:
		return {"ok": False, "error": "is used"}
	data[city][3] = True
	answer = " "
	for i in data:
		if (not data[i][3]) and low(i)[0] == low(city)[-1]:
			if answer == " " or data[answer][2] < data[i][2]:
				answer = i
	if answer == " ":
		return {"ok":True, "city": None}
	data[answer][3] = True
	return {"ok": True, "city": answer}
	

if __name__ == "__main__":
	get_reply(None, "Omom")