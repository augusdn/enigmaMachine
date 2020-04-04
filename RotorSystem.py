from Rotor import Rotor
from Reflector import Reflector

class RotorSystem:
    def __init__(self):
        self._rotorList = [ Rotor(wiring='EKMFLGDQVZNTOWYHXUSPAIBRCJ', notch="Q", name="I", model="Enigma 1", date="1930"),
                            Rotor(wiring="AJDKSIRUXBLHWTMCQGZNPYFVOE", notch="E", name="II", model="Enigma 1", date="1930"),
                            Rotor(wiring="BDFHJLCPRTXVZNYEIWGAKMUSQO", notch="V", name="III", model="Enigma 1", date="1930"),
                            Rotor(wiring="ESOVPZJAYQUIRHXLNFTGKDCMWB", notch="J", name="VI", model="M3 Army", date="December 1938"),
                            Rotor(wiring="VZBRGITYUPSDNHLXAWMJQOFECK", notch="Z", name="V", model="M3 Army", date="December 1938")]
        self._reflectorList = [
            Reflector(wiring="EJMZALYXVBWFCRQUONTSPIKHGD", name="Reflector A"),
            Reflector(wiring="YRUHQSLDPXNGOKMIEBFZCWVJAT", name="Reflector B"),
            Reflector(wiring="FVPJIAOYEDRZXWGCTKUQSBNMHL", name="Reflector C")
        ]
        self._rotors = [self._rotorList[0], self._rotorList[1], self._rotorList[2], self._reflectorList[1]]
# Rotors
    # def addRotorA(self, rotor):
    #     self._rotorA = rotor
    #     self._rotorA.reset()

    # def addRotorB(self, rotor):
    #     self._rotorB = rotor
    #     self._rotorB.reset()

    # def addRotorC(self, rotor):
    #     self._rotorC = rotor
    #     self._rotorC.reset()
    def changeRotor(self, t1, t2):
        self._rotors[t1] = self._rotorList[t2-1]

    def changePosition(self, t1, t2):
        self._rotors[t1-1]._position = ord(t2)-65
    
    def changeRing(self, t1, t2):
        self._rotors[t1-1].ringSettings(t2)
    
    def printSettings(self):
        for i in self._rotors:
            print(i)

    def rotate(self):
        if self._rotors[1].isNotch():
            for r in self._rotors:
                r.rotate()
        elif self._rotors[2].isNotch():
            self._rotors[1].rotate()
            self._rotors[2].rotate()
        else:
            self._rotors[2].rotate()
    
    def translate(self, c):
        self.rotate()
        results = []
        results.append(self._rotors[0].getPosition() + self._rotors[1].getPosition() + self._rotors[2].getPosition())
        r3 = self._rotors[2].translate(c)
        results.append(r3)
        r2 = self._rotors[1].translate(r3)
        results.append(r2)
        r1 = self._rotors[0].translate(r2)
        results.append(r1)
        reflector = self._rotors[3].translate(r1)
        results.append(reflector)
        r1 = self._rotors[0].reverse(reflector)
        results.append(r1)
        r2 = self._rotors[1].reverse(r1)
        results.append(r2)
        r3 = self._rotors[2].reverse(r2)
        results.append(r3)
        return results