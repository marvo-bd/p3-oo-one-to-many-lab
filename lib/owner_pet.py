class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner

        if self.pet_type not in Pet.PET_TYPES:
            raise Exception(f"{self.pet_type} is not a valid pet type")
        
        Pet.all.append(self)

class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def pets(self):
        """Return all pets owned by the owner."""
        return self._pets

    def add_pet(self, pet):
        """Add a pet to the owner's list if it's an instance of Pet."""
        if not isinstance(pet, Pet):
            raise Exception("You can only add a Pet instance.")
        pet.owner = self
        self._pets.append(pet)

    def get_sorted_pets(self):
        """Return a sorted list of pets by their names."""
        return sorted(self._pets, key=lambda pet: pet.name)
