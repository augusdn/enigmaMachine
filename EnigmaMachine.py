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
    def plugTwo(self, i1, i2):
        t1 = ord(i1.upper())-65
        t2 = ord(i2.upper())-65
        if t1 == t2:
            self.p("You can't plug same alphabet!")
        else:
            err = self._plugBoard.connectTwo(t1,t2)
            if err == 0:
                self.p(i1 + " is now paired with " + i2)
    # TODO: Add RotorSystem
    
    # TODO: Reflector
    
    # Encryption
    def encrypt(self, c):
        # convert input character to integer for easier conversion
        input = ord(c.upper())-65
        self.p("input char was " + c)
        # Plugboard
        plug_result = self._plugBoard.translate(input)
        self.p(chr(input+65) + "->" + chr(plug_result+65))

        result = plug_result
        result = chr(result+65)
        self.p(result)
        return result