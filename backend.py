data = {"Moscow":(1, 2, 100, 0)} # city:(lan, log, people, used)

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

def return_coordinates_city(city):
	if find_sity_in_data(city):
		return {city:(data[city][0], data[city][1])}
	return {city: None}


if __name__ == "__main__":
	print(return_coordinates_city("Moscow"))			