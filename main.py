from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, health: int):
        pass


class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer):
        pass

    @abstractmethod
    def detach(self, observer: Observer):
        pass

    @abstractmethod
    def notify(self):
        pass


class Player(Observer):
    def __init__(self, name, health=100):
        self.name = name
        self._health = health
        self.alerted = False 

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        if value <= 20 and not self.alerted:
            self._health = value
            self.alerted = True
            self.update(self._health)
        else:
            self._health = value

    def update(self, health: int):
        print(f"{self.name}, your health is critically low: {health}% left!")

class GameSystem(Subject):
    def __init__(self):
        self.players = []

    def attach(self, observer: Observer):
        self.players.append(observer)

    def detach(self, observer: Observer):
        self.players.remove(observer)

    def notify(self):
        for player in self.players:
            if player.health <= 20:
                player.update(player.health)

    def damage_player(self, player: Player, damage: int):
        if player in self.players:
            player.health -= damage

def main():
    player1 = Player("John")
    player2 = Player("Jane")

    game = GameSystem()
    game.attach(player1)
    game.attach(player2)

    game.damage_player(player1, 85) 
    game.damage_player(player2, 5)   
    
    game.detach(player2)
    game.damage_player(player2,90)

    

if __name__ == "__main__":
    main()
