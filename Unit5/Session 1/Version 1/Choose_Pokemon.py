class Pokemon:
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False

    def print_pokemon(self):
        print({
            "name": self.name,   
            "types": self.types, 
            "is_caught": self.is_caught 
        })
    
    def catch(self):
        self.is_caught = True
    
    def choose(self):
        if self.is_caught == True:
            print(self.name + " I choose you!")
        else:
            print(self.name + " is wild! Catch them if you can!")


my_pokemon = Pokemon("rattata", ["Normal"])
my_pokemon.print_pokemon()

my_pokemon.choose()
my_pokemon.catch()
my_pokemon.choose()