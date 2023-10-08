class Character:
    def __init__(self, name):
        self.name = name
        self.speed = 0
        self.energy = 100
        self.hp = 100
        self.damage = 10

    def display_stats(self):
        print(f"{self.name}: Speed={self.speed}, Energy={self.energy}, HP={self.hp}, Damage={self.damage}")

class Equipment(Character):
    def __init__(self, character):
        super().__init__(character.name)
        self.character = character

    def display_stats(self):
        self.character.display_stats()

class WingsEquipment(Equipment):
    def __init__(self, character):
        super().__init__(character)
        self.speed_bonus = 5
        self.energy_bonus = 20

    def apply(self):
        self.character.speed += self.speed_bonus
        self.character.energy += self.energy_bonus

class SwordEquipment(Equipment):
    def __init__(self, character):
        super().__init__(character)
        self.damage_bonus = 15

    def apply(self):
        self.character.damage += self.damage_bonus

class ArmorEquipment(Equipment):
    def __init__(self, character):
        super().__init__(character)
        self.hp_bonus = 50

    def apply(self):
        self.character.hp += self.hp_bonus

character = Character("Hero")
character.display_stats()



wings_equipment = WingsEquipment(character)
sword_equipment = SwordEquipment(character)
armor_equipment = ArmorEquipment(character)


wings_equipment.apply()
sword_equipment.apply()
armor_equipment.apply()

character.display_stats()
