class Player():
	def  __init__(self, character, kart):
		self.character = character
		self.kart = kart
		self.items = []
		
	def get_player(self):
		return f"{self.character} driving the {self.kart}"
		
	def set_player(self, name):
		valid_names = ["Mario", "Luigi", "Peach", "Yoshi", "Toad", "Wario", "Donkey Kong", "Bowser"]
		if name in valid_names:
			self.character = name
			print("Character updated")
		else:
			print("Invalid character")
	def add_item(self, item_name):
		valid_items = ["banana", "green shell", "red shell", "bob-omb", "super star", "lightning", "bullet bill"]
		if item_name in valid_items:
			self.items.append(item_name)
	def print_inventory(self):
		if len(self.items) == 0:
			print("Inventory empty")
		else:
			result = {}
			for i in range(len(self.items)):
				if self.items[i] not in result:
					result[self.items[i]] = 1
				else:
					result[self.items[i]] += 1
			print("Inventory:", end=" ")
			for key in result:
				if list(result).index(key) == len(result) - 1:
					print(key + ": " + str(result[key]))
				else:
					print(key + ": " + str(result[key]) + ",", end=" ")

def print_results(race_results):
	for i in range(len(race_results)):
		j = i + 1
		print(str(j) + ". " + race_results[i].character)

peach = Player("Peach", "Daytripper")
mario = Player("Mario", "Standard Kart M")
luigi = Player("Luigi", "Super Blooper")
race_one = [peach, mario, luigi]

print_results(race_one)