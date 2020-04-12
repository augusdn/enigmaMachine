from RotorSystem import RotorSystem
from Plugboard import PlugBoard

class EnigmaMachine:
    def __init__(self):
        self._plugBoard = PlugBoard()
        self._rotorSystem = RotorSystem()
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
    
    def changeRotor(self, t1, t2):
        self._rotorSystem.changeRotor(t1-1, t2)
        self._rotorSystem.printSettings()

    # Encryption
    def encrypt(self, c):
        # convert input character to integer for easier conversion
        self.p("Keyboard Input: " + c)
        # Plugboard
        plug_result = self._plugBoard.translate(c)
        self.p("Plugboard Encryption: " + plug_result)
        rotor_result = self._rotorSystem.translate(plug_result)
        if self._debugMode:
            print ("Rotors Position: " + rotor_result[0])
            print ("Wheel 3 Encryption: " + rotor_result[1])
            print ("Wheel 2 Encryption: " + rotor_result[2])
            print ("Wheel 1 Encryption: " + rotor_result[3])
            print ("Reflector Encryption: " + rotor_result[4])
            print ("Wheel 1 Encryption: " + rotor_result[5])
            print ("Wheel 2 Encryption: " + rotor_result[6])
            print ("Wheel 3 Encryption: " + rotor_result[7])
        plug_result = self._plugBoard.translate(rotor_result[7])
        self.p("Plugboard Encryption: " + plug_result)
        
        return plug_result