from RotorSystem import RotorSystem
from Plugboard import PlugBoard

class EnigmaMachine:
    def __init__(self):
        self._plugBoard = PlugBoard()
        self._rotorSystem = None
        self._reflector = None
        self._debugMode = False

    def p(self, str):
        if self._debugMode:
            print(str)

    def toggleDebug(self):
        if self._debugMode:
            self._debugMode = False
        else:
            self._debugMode = True

    # TODO: Add Plugboard
    def plugTwo(self, c1, c2):
        if c1 == c2:
            self.p("You can't plug same alphabet!")
        else:
            err = self._plugBoard.connectTwo(c1,c2)
            if err == 0:
                self.p(c1 + " is now paired with " + c2)
            elif err == -1:
                self.p(c1 + " is already plugged in!")
            elif err == -2:
                self.p(c2 + " is already plugged in!")
    # TODO: Add RotorSystem
    
    # TODO: Reflector
    
    # Encryption
    def encrypt(self, c):
        # convert input character to integer for easier conversion
        self.p("input char was " + c)
        # Plugboard
        plug_result = self._plugBoard.translate(c)
        self.p(c + "->" + c)

        result = plug_result
        
        self.p(result)
        return result