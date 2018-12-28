data = {"Moscow": [1, 2, 100, False], "Omom": [1, 2, 100, False]} # city:(lan, log, population, used)

user_stat = 0
comp_stat = 0
def _find_city_in_data(city):
	if(city in data):
		return True
	return False

def _to_low_format(word):
	if word is None:
		return word
	else:
		return word.lower()

def _to_city_format(word):
	if word is None:
		return word
	else:
		return word[0].upper() + word[1:].lower()

def get_statistic():
	return {"player": user_stat, "computer": comp_stat, "winner": "player" if user_stat >= comp_stat else "computer"}


def get_city_information(city):
	if _find_city_in_data(city):
		return {"coordinates": (data[city][0], data[city][1]), "population": data[city][2], "used": data[city][3]}
	return None

def get_reply(prev_city, city):
	city = _to_city_format(city)
	prev_city = _to_city_format(prev_city)
	if prev_city is None:
		prev_city = city[0].upper()
	if not _find_city_in_data(city):
		return {"ok": False, "error": "not in data"}
	elif (prev_city is not None) and (_to_low_format(prev_city[-1]) != _to_low_format(city[0])):
		return {"ok": False, "error": "mistake"}
	if get_city_information(city)["used"]:
		return {"ok": False, "error": "is used"}
	data[city][3] = True
	answer = " "
	for i in data:
		if (not data[i][3]) and (_to_low_format(i)[0] == _to_low_format(city)[-1]):
			if answer == " " or data[answer][2] < data[i][2]:
				answer = i
	if answer == " ":
		return {"ok": True, "city": None}
	data[answer][3] = True
	return {"ok": True, "city": answer}
	

if __name__ == "__main__":
	print(get_reply(None, "Omom"))