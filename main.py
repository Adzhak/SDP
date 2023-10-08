class MovementStrategy:
    def move(self, character):
        pass

class WalkStrategy(MovementStrategy):
    def move(self, character):
        character.speed = 1
        character.energy += 10
        print(f"Character is walking (Speed: {character.speed}, Energy: {character.energy})")

class RunStrategy(MovementStrategy):
    def move(self, character):
        if character.energy >= 20:
            character.speed = 3
            character.energy -= 20
            print(f"Character is running (Speed: {character.speed}, Energy: {character.energy})")
        else:
            print("Not enough energy to run.")

class FlyStrategy(MovementStrategy):
    def move(self, character):
        if character.energy >= 50:
            character.speed = 5
            character.energy -= 50
            print(f"Character is flying (Speed: {character.speed}, Energy: {character.energy})")
        else:
            print("Not enough energy to fly.")

class Character:
    def __init__(self, movement_strategy):
        self.movement_strategy = movement_strategy
        self.speed = 0
        self.energy = 100

    def perform_move(self):
        self.movement_strategy.move(self)

class Equipment(MovementStrategy):
    def __init__(self, get_equipment):
        self.get_equipment = get_equipment

    def move(self, character):
        self.get_equipment.move(character)

class WingsEquipment(Equipment):
    def move(self, character):
        self.get_equipment.move(character)
        character.speed += 1  

class PotionEquipment(Equipment):
    def move(self, character):
        self.get_equipment.move(character)
        character.energy += 10  

character1 = Character(WalkStrategy())
character1_with_sword = Character(WingsEquipment(character1))
character1_with_armor = Character(PotionEquipment(character1))

character1.perform_move() 
character1_with_sword.perform_move()  
character1_with_armor.perform_move()  