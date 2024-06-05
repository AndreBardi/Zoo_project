class Zoo:
    def __init__(self,
                 fences: list,
                 zoo_keepers: list):
        
        self.fences = fences
        self.zoo_keepers = zoo_keepers

    def describe_zoo(self):
        print("Guardians:")
        for zoo_keeper in self.zoo_keepers:
            print(zoo_keeper)

        print("\nFences:")
        for fence in self.fences:
            print(fence)
            print("with animals:")
            for animal in fence.animals:
                print(animal)

        print("#" * 30)


class Animal:
    def __init__(self,
                name: str, 
                species: str, 
                age: int, 
                height: float, 
                width: float, 
                preferred_habitat: str):
       
        self.name: str = name
        self.species: str = species
        self.age: int = age
        self.height: float = height
        self.width: float = width
        self.preferred_habitat: str = preferred_habitat
        self.health: float = round(100 * (1 / age), 3)
        self.area = height * width

    def __str__(self):
        return f"Animal(name={self.name}, species={self.species}, age={self.age}, health={self.health})"

class Fence:
    def __init__(self, 
                 area: float, 
                 temperature: float, 
                 habitat: str, ):
        
        self.initial_area = area
        self.area: float = area
        self.temperature: float = temperature
        self.habitat: str = habitat
        self.animals: list = []
    
    def __str__(self):
            return f"Fence(area={self.initial_area}, temperature={self.temperature}, habitat={self.habitat})"

class Zoo_keeper:
    def __init__(self,
                 name: str,
                 surname: str,
                 id: str,
                 zoo: str):
        
        self.name: str = name
        self.surname: str = surname
        self.id: str = id
        self.fences: list = []
        self.animals: list = []
        self.zoo: str = zoo

    def add_animal(self, animal: Animal, fence: Fence):
        if fence in self.zoo.fences and fence.area >= animal.area:
            fence.area -= animal.area
            fence.animals.append(animal)
            

    def remove_animal(self, animal: Animal, fence: Fence):
        if fence in self.zoo.fences and animal in fence.animals:
            fence.area += animal.area
            fence.animals.remove(animal)
   
    def feed(self):
        for fence in self.zoo.fences:
            for animal in fence.animals:
                self.feed_animal(animal, fence)

    def feed_animal(self, animal, fence):
        new_height = animal.height * 1.02
        new_width = animal.width * 1.02
        required_space = new_height * new_width - animal.height * animal.width

        if animal.health < 100 and fence.area >= required_space:
            animal.health = min(100, animal.health + 1)
            fence.area -= required_space
            animal.height = new_height
            animal.width = new_width

    def clean(self):
        cleaning_time = 0.0
        for fence in self.fences:
            cleaning_time += self.cleaning_the_fence(fence)
        return cleaning_time

    def cleaning_the_fence(self, fence: Fence):
        occupied_area = sum(animal.area for animal in fence.animals)
        if fence.area == 0:
            return occupied_area
        else: 
            return occupied_area / fence.area
        
    def __str__(self):
        return f"ZooKeeper(name={self.name}, surname={self.surname}, id={self.id})"
