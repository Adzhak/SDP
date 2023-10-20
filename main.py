class GamePlatform:
    def start(self): pass
    def save(self): pass
    def exit(self): pass

class PCPlatform:
    def bootGame(self): return "Booting game on PC"
    def writeSaveFile(self): return "Saving game data on PC"
    def closeGame(self): return "Closing game on PC"

class ConsolePlatform:
    def launchGame(self): return "Launching game on Console"
    def saveToConsoleMemory(self): return "Storing game data on Console"
    def shutGame(self): return "Shutting down game on Console"

class MobilePlatform:
    def runApp(self): return "Running game app on Mobile"
    def saveToMobileStorage(self): return "Saving game state on Mobile"
    def closeApp(self): return "Closing game app on Mobile"


class PCAdapter(GamePlatform):
    def __init__(self, platform):
        self.platform = platform
    def start(self): return self.platform.bootGame()
    def save(self): return self.platform.writeSaveFile()
    def exit(self): return self.platform.closeGame()

class ConsoleAdapter(GamePlatform):
    def __init__(self, platform):
        self.platform = platform
    def start(self): return self.platform.launchGame()
    def save(self): return self.platform.saveToConsoleMemory()
    def exit(self): return self.platform.shutGame()

class MobileAdapter(GamePlatform):
    def __init__(self, platform):
        self.platform = platform

    def start(self): return self.platform.runApp()
    def save(self): return self.platform.saveToMobileStorage()
    def exit(self): return self.platform.closeApp()



def playGameOnPlatform(platform: GamePlatform):
    print(platform.start())
    print(platform.save())
    print(platform.exit())


pc = PCPlatform()
console = ConsolePlatform()
mobile = MobilePlatform()

pcAdapter = PCAdapter(pc)
consoleAdapter = ConsoleAdapter(console)
mobileAdapter = MobileAdapter(mobile)

print("Playing on PC:")
playGameOnPlatform(pcAdapter)

print("Playing on Console:")
playGameOnPlatform(consoleAdapter)

print("Playing on Mobile:")
playGameOnPlatform(mobileAdapter)