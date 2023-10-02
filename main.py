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

character1 = Character(WalkStrategy())
character1.perform_move()

character2 = Character(RunStrategy())
character2.perform_move()

character3 = Character(FlyStrategy())
character3.perform_move()
