class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    all = []
    def __init__(self, name, pet_type, owner=None):
        if pet_type in self.PET_TYPES:
            self.name = name
            self.pet_type = pet_type
            self.owner = owner
            Pet.all.append(self)
        else:
            raise Exception

class Owner:
    def __init__(self, name):
        self.name = name
        self.pets_list = []
    def pets(self):
        return Pet.all
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception
        pet.owner = self
        self.pets_list.append(pet)
        
    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)

